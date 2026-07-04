from flask import Flask
from flask_migrate import Migrate
from config import config  
from db import db


app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

from app.models import (
    category_model,
    role_model,
    user_model,
    event_model,
    booking_model
)

from app import router