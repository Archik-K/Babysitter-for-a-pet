"""
Environment requirements:

    Flask:
        DEBUG
            type: int | None
            default: 0
            description:
                0 - False
                1 - True
"""

from os import environ, getenv, sep
from pathlib import Path

__all__ = ["Config"]


class Config:
    BASE_DIR = str(Path(__file__).resolve().parent.parent).replace(sep, "/")
    DEBUG_MODE = bool(int(getenv("DEBUG", 0)))

    SQLALCHEMY_DATABASE_URI = environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SWAGGER_FORMS = BASE_DIR + "/swagger_forms/"
    UPLOAD_FOLDER = BASE_DIR + "/media/"

