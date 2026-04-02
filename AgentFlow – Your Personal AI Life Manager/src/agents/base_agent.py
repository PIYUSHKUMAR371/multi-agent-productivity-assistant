from google.adk import Agent
from src.config.settings import settings

class BaseSubAgent(Agent):
    """Base class for all sub-agents"""
    def __init__(self, name: str, description: str, instructions: str):
        super().__init__(
            name=name,
            model=settings.GEMINI_MODEL,
            description=description,
            instructions=instructions,
        )