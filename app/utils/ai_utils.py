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
    generation_config=generate_config(TypedDict("DictionarySchema", {
        "definition": "str", 
        "part_of_speech": "str", 
        "example_sentence": "str"
    })),
    system_instruction="Given a word and a context in the format of {word: word, context: message}, generate a response that provides the definition of the word, and uses the word in an example sentence.",
)

# social context bot
social_context_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generate_config(TypedDict("SocialContextSchema", {
        "response": "str"
    })),
    system_instruction="Given a message, message history, and social context in the format of {message:message, messageHistory: [{role:role, text:message}], receiver_role: receiver_role_details}, generate a response that analyzes how the user's message might be received in the context of the message history and how appropriate the message is. The response should include information about the social norms and expectations that are relevant to the situation presented in the message history and social context. Keep the response under 1000 characters.",
)

# example response bot
example_response_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generate_config(TypedDict("ExampleResponseSchema", {"example_response": "str", "explanation": "str"})),
    system_instruction="Given a message, message history, and social context in the format of {message:message from conversation partner, messageHistory: [{role:role, text:message}], socialContext: {user: messageReceiver, conversationPartner: messageSender, situation: situation}},  generate an example response to the message that the user could use in the given social context. The response should include an explanation regarding what the conversation partner might expect from the user's response and what the model's example response communicates. The example response should be 255 characters or less.",
)