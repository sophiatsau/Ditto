# history: record / memory of conversation.
# using an object so that it can be changed between files: logging out = clearing history
"""
[
  {
    "role": "user" or "model",
    "parts": ["text"]
  }
]
"""
# TODO: delete this, update
history = {"history":[]}


# grammar bot


# definition bot


# social context bot


# example response bot


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