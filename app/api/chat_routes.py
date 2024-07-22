from flask import Blueprint
from flask_login import login_required
from .utils import history
import os
import google.generativeai as genai
# from google.generativeai.types import HarmCategory, HarmBlockThreshold


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# create, config model
generation_config = {
  "temperature": 0, # 0 = more factual, 1 = more creative
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain", # "application/json"
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  # safety_settings={
  #       HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
  #       HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
  #       HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
  #       HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
  #       HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
  #   },
  system_instruction="You are the user's best buddy. If there is a probability of unsafe content in model response, warn the user and generate a response without unsafe content.",
)


chat_routes = Blueprint('chat', __name__)


@chat_routes.route('/')
#@login_required
def test():
    """test route"""
    return {"msg":"chat route entered", "history": history}, 200


@chat_routes.route('/<int:chat_id>')
#@login_required
def load_chat(chat_id):
    """
    loads content of previously saved conversation
    """
    # find the convo + associated messages
    # return them
    global history
    history = ["Message contents"]
    return {"Conversation": [{"Message":"Message Contents"}]}, 200


@chat_routes.route('/new')
#@login_required
def new_chat():
    """
    create a new conversation
    """
    return


@chat_routes.route('/grammar/<int:msg_id>')
#@login_required
def check_grammar(msg_id):
    """
    check grammar for a specific message
    """
    # use a different model with instructions to check grammar
    # return grammar feedback for specific msg