from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict

# import os
# load_dotenv = os.getenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    app_name: str = "IT-Support-RAG-Copilot"
    app_env: str = "dev"
    groq_api_key: str = ""
    tavily_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_index_name: str = "it-support-rag-copilot"
    pinecone_namespace: str = "company-it-kb"
    openai_model: str = ""
    groq_model: str = ""
    top_k: int = 4
    max_retries:int = 1

    admin_api_key: str = "change this" #admin password for the API endpoints, change this in production

    audit_db_path: str = str(BASE_DIR / "data" / "audit.db") #sqlite
    # audit_db_url: str = os.getenv("AUDIT_DATABASE_URL", "") #postegres

    uploads_dir: str = str(BASE_DIR / "uploads")  #for production ready you have to change this to any cloud services

    sample_kb_dir:str = str(BASE_DIR / "data" / "sample_kb") #sample knowledge base for testing

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"),extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()