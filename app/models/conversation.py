from .db import db, environment, SCHEMA, add_prefix_for_prod
import os

import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# create, config model
generation_config = {
  "temperature": 0, # 0 = more factual, 1 = more creative
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain", # "application/json"
}

class Conversation(db.Model):
    """
    Conversation between user and chatbot, one-to-many relationship with messages
    """
    __tablename__ = "conversations"
    # __chatbot_info__ = {} # save models
    # __chat_session_info__ = {} # save chat sessions

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    system_instructions = db.Column(db.String(255), nullable=False, default="If there is a probability of unsafe content in model response, warn the user and generate a response without unsafe content.")

    # def __init__(self):
    #     self.chatbot, self.chat_session = None, None

    user = db.relationship(
        "User",
        back_populates="conversations"
    )

    messages = db.relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )

    @property
    def history(self):
        """format for history object"""
        return [message.to_history() for message in self.messages]
    
    def get_chatbot(self):
        """create + return ai model for this conversation"""
        return genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                generation_config=generation_config,
                system_instruction=self.system_instructions,
            )
        # return self.__chatbot_info__[self.user_id]
    
    def get_convo_session(self):
        """create + return convo session for this conversation"""
        return self.get_chatbot().start_chat(history = self.history)
        # return self.__chat_session_info__[self.user_id]

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'system_instructions': self.system_instructions,
            'history': [message.to_dict() for message in self.messages],
        }