from flask import Blueprint, request, redirect, session
from flask_login import login_required, current_user
# from .utils import history
from app.utils.ai_utils import grammar_bot, dictionary_bot, social_context_bot, example_response_bot
import os
import google.generativeai as genai
# from google.generativeai.types import HarmCategory, HarmBlockThreshold

from app.models import db, Conversation, Message
from app.forms import MessageForm, ConversationForm


# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# create, config model
generation_config = {
  "temperature": 0, # 0 = more factual, 1 = more creative
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain", # "application/json"
}

# model, chat_session = None, None

#***************** Routes *****************#
chat_routes = Blueprint('chat', __name__)


@chat_routes.route('/')
@login_required
def test():
    """test route"""
    return {"msg":"chat route entered", **history}, 200


#***************** Conversations *****************#
@chat_routes.route('/<int:conversation_id>')
@login_required
def load_conversation(conversation_id):
    """
    loads content of previously saved conversation
    """

    # retrieve conversation
    convo = Conversation.query.get(conversation_id)
    if not convo or convo.user_id != current_user.id:
        return {"error":"Conversation not found"}, 404

    return {"conversation": convo.to_dict()}, 200


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

    convo = Conversation(
        user_id=current_user.id,
        system_instructions=system_instructions,
    )

    db.session.add(convo)
    db.session.commit()

    return {"conversation": convo.to_dict()}, 201


@chat_routes.route('/<int:chat_id>/delete', methods=["DELETE"])
@login_required
def delete_chat(chat_id):
    """
    delete a conversation
    """
    convo = Conversation.query.get(chat_id)
    if not convo or convo.user_id != current_user.id:
        return {"error":"Conversation not found"}, 404

    db.session.delete(convo)
    db.session.commit()

    return {"message":"Conversation deleted"}, 200


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

    # send message to model + get response
    response = convo.get_convo_session().send_message(input)

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

    return {"messages": [user_msg.to_dict(), model_msg.to_dict()], "chat_id": chat_id}, 201


#***************** FEEDBACK BOTS *****************#
@chat_routes.route('/grammar/<int:msg_id>')
@login_required
def check_grammar(msg_id):
    """
    check grammar for a specific message and return {
        "errors_present": "bool", 
        "corrected_message": "str", 
        "explanation": "str"
    }
    """
    message = Message.query.get(msg_id)
    if not message:
        return {"error":"Message not found"}, 404
    response = grammar_bot.generate_content(f"{{message: {message.text}}}")
    res = response.text
    return res, 200


@chat_routes.route('/message/<int:msg_id>/definition/<word>')
@login_required
def get_definition(msg_id, word):
    """
    get definition of a specific word in the context of a message and return {
        "definition": "str", 
        "part_of_speech": "str", 
        "example_sentence": "str"
    }
    """
    message = Message.query.get(msg_id)
    if not message:
        return {"error": "Message not found"}, 404
    if not word or word not in message.text:
        return {"error": "Word not found in message"}, 400
    response = dictionary_bot.generate_content(f"{{word: {word}, context: {message.text}}}")
    res = response.text
    return res, 200


@chat_routes.route('/<int:chat_id>/message/<int:msg_id>/social')
@login_required
def check_social_context(chat_id, msg_id):
    """
    check social appropriateness of a specific message in context of the conversation and return {"response": "str"}
    """
    convo = Conversation.query.get(chat_id)
    history = convo.history
    if not convo:
        return {"error": "Conversation not found"}, 404
    [message] = [msg for msg in convo.messages if msg.id == msg_id]
    if not message:
        return {"error": "Message not found"}, 404
    response = social_context_bot.generate_content(f"{{message:{message.text}, message_history: {history}, receiver_role: convo.system_instructions}}")
    res = response.text
    return res, 200


@chat_routes.route('/<int:chat_id>/message/<int:msg_id>/response')
@login_required
def generate_example_response(chat_id, msg_id):
    """
    generate example response for a specific message in context of the conversation and return {"example_response": "str", "explanation": "str"}
    """
    convo = Conversation.query.get(chat_id)
    history = convo.history
    if not convo:
        return {"error": "Conversation not found"}, 404
    [message] = [msg for msg in convo.messages if msg.id == msg_id]
    if not message:
        return {"error": "Message not found"}, 404
    response = example_response_bot.generate_content(f"{{message:{message.text}, message_history: {history}, conversation_partner_role: {convo.system_instructions}}}")
    res = response.text
    return res, 200