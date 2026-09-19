
from database import base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime,timezone
import uuid

class Conversation(base):
    __tablename__ = "conversations"
    id = Column(UUID(as_uuid=True),primary_key=True,default = uuid.uuid4)
    created_at = Column(DateTime,datetime.now(timezone.utc))
    messages = relationship("Message", back_populates="conversation_id")

class Message(base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    created_at = Column(DateTime,datetime.now(timezone.utc))
    content = Column(String(500))
    role = Column(String(50))
    conversation_id = relationship("Conversation",back_populates="messages")


class Note(base):
    __tablename__ = "notes"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    content = Column(String(500))
    created_at = Column(DateTime(datetime.now(timezone.utc)))