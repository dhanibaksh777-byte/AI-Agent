from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class ConversationResponse(BaseModel):
    id : UUID
    created_at : datetime

class CreateMessage(BaseModel):
    content : str

class MessageResponse(BaseModel):
    id : UUID
    role : str
    content : str
    created_at : datetime

class NoteCreate(BaseModel):
    content : str

class NoteResponse(BaseModel):
    id : UUID
    content : str
    created_at : datetime