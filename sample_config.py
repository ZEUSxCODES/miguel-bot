import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 6))

    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    
    OWNER_ID = os.environ.get("OWNER_ID", "")
    
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
