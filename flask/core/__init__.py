from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_restful import Api

from .config import Config
from apps import route_resources

__all__ = ["app", "api", "db", "Config"]

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


# SWAGGER_TEMPLATE = {
#     "securityDefinitions": {
#         "APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}
#     }
# }
# Swagger(app, template=SWAGGER_TEMPLATE)
Swagger(app)

db = SQLAlchemy(app)

route_resources()
