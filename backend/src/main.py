import os
from fastapi import FastAPI

app = FastAPI()

PROJECT = os.environ.get("PROJECT") or "Docker FastAPI"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API_KEY not set in environment variables")

@app.get("/")
def read_index():
    return {"Hello": "Dockerss!", "Project": PROJECT}