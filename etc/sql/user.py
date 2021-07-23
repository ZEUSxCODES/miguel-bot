from sqlalchemy import (
    Column,
    String,
    Integer
)
from . import (
    SESSION,
    BASE
)


class Users(BASE):
    """ Table to store the received messages """
    __tablename__ = "users"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    um_id = Column(Integer)

    def __init__(self, message_id, chat_id, um_id):
        self.message_id = message_id
        self.chat_id = str(chat_id)  # ensure string
        self.um_id = um_id

    def __repr__(self):
        return "<User %s>" % self.chat_id


Users.__table__.create(checkfirst=True)


def his_userid(message_id: int):
    """ get the user_id from the message_id """
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        return int(s__.chat_id), s__.um_id
    finally:
        SESSION.close()
