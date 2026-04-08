from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.primary_agent import primary_agent

app = FastAPI(title="Multi-Agent Productivity Assistant")

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    response = primary_agent(req.message)
    return {
        "status": "success",
        "response": response
    }

@app.get("/tasks")
def get_all_tasks():
    from src.agents.task_agent import get_tasks
    return {
        "status": "success",
        "tasks": get_tasks()
    }

@app.get("/health")
def health_check():
    return {"status": "running"}