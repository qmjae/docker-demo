from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def chat_health_check():
    return {"status": "Chat API is healthy"}