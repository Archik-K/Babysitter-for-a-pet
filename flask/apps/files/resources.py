from werkzeug.exceptions import NotFound
from flask_restful import Resource
from flasgger import swag_from
from core import Config
from flask import send_from_directory


class FileResource(Resource):
    @swag_from(Config.SWAGGER_FORMS + 'file_get.yml')
    def get(self, path):
        try:
            return send_from_directory(Config.UPLOAD_FOLDER, path)
        except NotFound:
            return "File is not found, or you don't have access", 404
