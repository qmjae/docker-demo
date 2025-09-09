import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db import init_db
from api.chat.routing import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    init_db()
    yield
    #shutdown
    print("Shutting down database...")

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")

PROJECT = os.environ.get("PROJECT") or "Docker FastAPI"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API_KEY not set in environment variables")

@app.get("/")
def read_index():
    return {"status": "ok!"}