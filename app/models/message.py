from .db import db, environment, SCHEMA, add_prefix_for_prod

class Message(db.Model):
    __tablename__ = "messages"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('conversations.id')), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    text = db.Column(db.String(255), nullable=False)

    conversation = db.relationship(
        "Conversation",
        back_populates="messages"
    )

    def to_history(self):
        """format for history object"""
        return {
            'role': self.role,
            'parts': [self.text],
        }

    def to_dict(self):
        return {
            'id': self.id,
            # 'conversation_id': self.conversation_id,
            'role': self.role,
            'parts': [self.text],
        }