from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session
from .models import ChatMessagePayload, ChatMessage

router = APIRouter()

@router.get("/")
def chat_health_check():
    return {"status": "Chat API is healthy"}

@router.get("/recent")
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10] #fetch all chat messages
    return results

#curl -X POST -d '{"message": "Hello"}' -H "Content-Type: application/json" http://localhost:8080/api/chats/
@router.post("/", response_model=ChatMessage)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj