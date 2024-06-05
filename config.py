import os

from dotenv.main import load_dotenv

load_dotenv()

# Discord config
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
DEBUG = os.getenv("DEBUG")
AUTO_RELOAD = os.getenv("AUTOLOAD")
BOT_PREFIX = "!"
COGS_DIR = "cogs"
LOAD_EXCEPTIONS = []
