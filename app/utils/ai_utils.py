import os
from typing_extensions import TypedDict

import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_config(response_schema):
    return {
        "temperature": 0, # 0 = more factual, 1 = more creative
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json", # "application/json"
        "response_schema": response_schema, # {}
    }

# errors_present = NewType("errors_present", bool)
# corrected_message = NewType("corrected_message", str)
# explanation = NewType("explanation", str)

# GrammarSchema = dict[errors_present, corrected_message, explanation]

# grammar bot
grammar_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generate_config(TypedDict("GrammarSchema", {
        "errors_present": "bool", 
        "corrected_message": "str", 
        "explanation": "str"
    })),
    system_instruction="Given a message in the format of {message: message}, generate a response that includes 1. the message with corrected grammar and 2. an explanation of what grammatical rules were broken. If no grammatical errors are present, generate a response that includes the original message and an explanation that no grammatical errors were found.",
)

# definition bot
dictionary_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    # generation_config=generate_config({
    #     "definition": "str", 
    #     "part_of_speech": "str", 
    #     "exampleSentence": "str"
    # }),
    system_instruction="Given a word and a context in the format of {word: word, context: message}, generate a response that provides the definition of the word, and uses the word in an example sentence.",
)

# social context bot
social_context_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    # generation_config=generate_config({
    #     "response": "str"
    # }),
    system_instruction="Given a message, message history, and social context in the format of {message:message, messageHistory: [{role:role, text:message}], socialContext: {user: messageSender, receiver: messageReceiver, situation: situation}}, generate a response that analyzes how the user's message might be received in the context of the message history and how appropriate the message is. The response should include information about the social norms and expectations that are relevant to the situation presented in the message history and social context.",
)

# example response bot
example_response_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    # generation_config=generation_config,
    system_instruction="Given a message, message history, and social context in the format of {message:message from conversation partner, messageHistory: [{role:role, text:message}], socialContext: {user: messageReceiver, conversationPartner: messageSender, situation: situation}},  generate an example response to the message that the user could use in the given social context. The response should include an explanation regarding what the conversation partner might expect from the user's response and what the model's example response communicates. The response should be formatted as {response: response, explanation: explanation}.",
)


"""
chat_histories = {
 [user_id]: {
    chat_id: {
      ChatBot Class
    }
 }
}


class ChatBot():
    def __init__(self, prompt, user):
        # initiate conversation with prompt and user
        self.chat_session = ChatSession()
    
    def send_message(self, input):
        response = self.chat_session.send_message(input)
        # add response to history
        history["history"].append({"role":"user", "parts":[input]})
        history["history"].append({"role":"model", "parts":[response.text]})
        return response


"""