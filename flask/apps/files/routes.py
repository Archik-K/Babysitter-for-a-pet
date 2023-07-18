from core import api
from .resources import FileResource


def route_resources():
    api.add_resource(FileResource, "/file/<path:path>")
