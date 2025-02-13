import os

from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv("LOGIN")
PHONE = os.getenv("PHONE")
PASSWORD = os.getenv("PASSWORD")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CLOWN_ID = os.getenv("CLOWN_ID")

log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", None)
log_format = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")