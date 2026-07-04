from dotenv import load_dotenv
import os

load_dotenv()

class config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    
    
