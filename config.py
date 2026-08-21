import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ORIGIN = os.getenv("ORIGIN")
    DB_URL = os.getenv("DB_URL")

setting = settings()
