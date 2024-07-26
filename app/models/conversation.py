from .db import db, environment, SCHEMA, add_prefix_for_prod

class Conversation(db.Model):
    """
    Conversation between user and chatbot, one-to-many relationship with messages
    """
    __tablename__ = "conversations"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    system_instructions = db.Column(db.String(255), nullable=False, default="If there is a probability of unsafe content in model response, warn the user and generate a response without unsafe content.")

    user = db.relationship(
        "User",
        back_populates="conversations"
    )

    messages = db.relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )

    def to_history(self):
        """format for history object"""
        return {
            'history': [message.to_history() for message in self.messages],
        }

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'system_instructions': self.system_instructions,
            'history': [message.to_dict() for message in self.messages],
        }