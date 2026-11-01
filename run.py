from app.core.config import get_settings

settings = get_settings()

print("My project name is:", settings.app_name)
print("My project environment is:", settings.app_env)