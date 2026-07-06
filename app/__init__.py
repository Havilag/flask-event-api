from flask import Flask
from flask_migrate import Migrate
from config import Config  
from db import db
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Gestión de Eventos y Reservas"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from app.models import (
    category_model,
    role_model,
    user_model,
    event_model,
    booking_model
)

from app import router