import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6813230293:AAEzC1y8PyZMVMFCxQ9O_hkVISXrcLTD-rs")

    APP_ID = int(os.environ.get("APP_ID", 20434292))

    API_HASH = os.environ.get("API_HASH", "ea4683f64ac46aa1d6fb236638a0ac01")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1663603208))
    
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Anmol0700")
