from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response

app = FastAPI()


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_response(request.message)
    return {"response": reply}