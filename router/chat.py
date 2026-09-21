from fastapi import APIRouter,Depends,HTTPException,status
from agent.runner import get_responses
from sqlalchemy.orm import Session
from models import Conversation,Message,Note
from database import get_db
from schemas import CreateMessage

router = APIRouter()

@router.post("/conversation")
def new_conversation(db : Session = Depends(get_db)):
    conv = Conversation()
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return {"id": str(conv.id), "created_at": str(conv.created_at)}


@router.post("/chat/{conversation_id}")
def chat(message : CreateMessage,conversation_id : str,db : Session = Depends(get_db)):
    chats = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not chats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="chat not found!")
    result = get_responses(message.content, db,conversation_id)
    return result



    
