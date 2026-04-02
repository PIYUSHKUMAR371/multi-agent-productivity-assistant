from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    GOOGLE_CLOUD_PROJECT: str
    GOOGLE_CLOUD_LOCATION: str = "us-central1"
    GEMINI_MODEL: str = "gemini-2.0-flash-exp"
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Singleton instance
settings = Settings()
