import os
from dotenv import load_dotenv

load_dotenv('.env')
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


