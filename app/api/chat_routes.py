from flask import Blueprint, request, redirect
from flask_login import login_required, current_user
from .utils import history
import os
import google.generativeai as genai
# from google.generativeai.types import HarmCategory, HarmBlockThreshold

from app.models import db, Conversation, Message
from app.forms import MessageForm, ConversationForm


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# create, config model
generation_config = {
  "temperature": 0, # 0 = more factual, 1 = more creative
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain", # "application/json"
}

model, chat_session = None, None


#***************** Routes *****************#
chat_routes = Blueprint('chat', __name__)


@chat_routes.route('/')
@login_required
def test():
    """test route"""
    return {"msg":"chat route entered", **history}, 200


#***************** Conversations *****************#
@chat_routes.route('/<int:chat_id>')
@login_required
def load_chat(chat_id):
    """
    loads content of previously saved conversation
    """
    convo = Conversation.query.get(chat_id)
    if not convo:
        return {"error":"Conversation not found"}, 404
    if convo.user_id != current_user.id:
        return {"error":"Unauthorized"}, 401

    global model
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=convo.system_instructions,
    )
    
    history["history"] = convo.to_history()["history"]
    global chat_session
    chat_session = model.start_chat(history=history["history"])
    return {"Conversation": convo.to_dict()}, 200


@chat_routes.route('/new', methods=["POST"])
@login_required
def new_chat():
    """
    create a new conversation
    """
    # validate form
    form = ConversationForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        system_instructions = form.system_instructions.data
    else:
        return {"errors":form.errors}, 400

    global model
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=system_instructions,
    )

    global chat_session
    global history
    history["history"] = []
    chat_session = model.start_chat(history=[])

    convo = Conversation(
        user_id=current_user.id,
        system_instructions=system_instructions,
    )

    db.session.add(convo)
    db.session.commit()

    return convo.to_dict(), 200


#***************** Messages *****************#
@chat_routes.route('/<int:chat_id>/send', methods=["POST"])
@login_required
def send_message(chat_id):
    """
    send a new message in the conversation
    """
    # TODO: time stamp?
    # check if conversation exists
    convo = Conversation.query.get(chat_id)
    if not convo:
        return {"error":"Conversation not found"}, 404

    # validate message
    form = MessageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        input = form.text.data
    else:
        return {"errors":form.errors}, 400

    # send message to model
    # TODO: chat session created in here instead of global
    global chat_session
    response = chat_session.send_message(input)

    # add response to history
    global history
    history["history"].append({"role":"user", "parts":[input]})
    history["history"].append({"role":"model", "parts":[response.text]})

    # create messages + add to db
    user_msg = Message(
        conversation_id=chat_id,
        role="user",
        text=input,
    )

    model_msg = Message(
        conversation_id=chat_id,
        role="model",
        text=response.text,
    )

    db.session.add_all([user_msg, model_msg])
    db.session.commit()

    return [user_msg.to_dict(), model_msg.to_dict()], 200


# TODO: a grammar / spelling / context checking bot?
@chat_routes.route('/grammar/<int:msg_id>')
@login_required
def check_grammar(msg_id):
    """
    check grammar for a specific message
    """
    # use a different model with instructions to check grammar
    # return grammar feedback for specific msg