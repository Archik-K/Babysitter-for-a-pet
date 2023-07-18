from core import api
from .resources import NannyResource


def route_resources():
    api.add_resource(NannyResource, "/nanny")
