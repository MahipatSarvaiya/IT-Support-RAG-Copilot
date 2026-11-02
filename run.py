# from app.core.config import get_settings

# settings = get_settings()

# print("My project name is:", settings.app_name)
# print("My project environment is:", settings.app_env)


from app.services.ingestion import load_file, chunk_documents
from pathlib import Path

docs = load_file(Path("data/sample_kb/company_handbook.md"))
docs1 = chunk_documents(docs)

print(docs)
print(len(docs1))

