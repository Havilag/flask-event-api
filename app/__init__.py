from flask import Flask
from flask_migrate import Migrate
from config import Config  
from db import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app.models import (
    category_model,
    role_model,
    user_model,
    event_model,
    booking_model
)

from app import router