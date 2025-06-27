from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
def chat(input: ChatInput):
    reply = agent.handle_input(input.message)
    return {"response": reply}