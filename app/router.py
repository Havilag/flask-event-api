from flask_restful import Api
from app import app

api = Api(app, prefix='/app/v1')