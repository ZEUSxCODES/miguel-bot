import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", ))

    API_HASH = os.environ.get("API_HASH", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", ))
    
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
