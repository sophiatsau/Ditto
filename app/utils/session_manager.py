#

from app.models import db, Conversation

class SessionManager:
    # get, create session
    def get_session(self, convo_id):
        return Conversation.query.get(convo_id)
        

    # save context

    # (will load session manager in chat_routes when a conversation is loaded or created)
    pass