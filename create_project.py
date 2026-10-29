from pathlib import Path

# current working directory
root = Path(".")

#folder to create 

folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

# files to create
files = [
    "app/main.py",
    "requirements.txt",
    "ingest_sample_kb.py",
    "run.py",
    ".env"
]

#create folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    (root / file).touch(exist_ok=True)

print("Project structure created successfully.")