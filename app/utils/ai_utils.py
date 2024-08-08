import os

import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 0, # 0 = more factual, 1 = more creative
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain", # "application/json"
}

# grammar bot
grammar_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Given a sentence, generate a response that corrects and explains any grammatical errors in the sentence. Praise the user if the sentence is grammatically correct.",
)

# definition bot
dictionary_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Given a word and a context in the format of {word: word, context: message}, generate a response that provides the definition of the word, and uses the word in an example sentence.",
)

# social context bot
social_context_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Given a message, message history, and social context in the format of {message:message, message_history: [], social_context: {sender: person saying the message, receiver: person receiving the message, situation: situation}}, generate a response that analyzes how the message might be received in the context of the message history and how appropriate the message is. The response should include information about the social norms and expectations that are relevant to the situation presented in the message history and social context.",
)

# example response bot
example_response_bot = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Given a message and social context in the format of {message: message, social_context: social_context}, generate an example response to the message in the given social context. The response should include information about the context in which the sentence is used, and the people who might use it.",
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