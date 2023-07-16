from .exceptions import BaseServerException
from core import Config


def exception_catcher_decorator(method):
    def inner(*args, **kwargs):
        try:
            response = method(*args, **kwargs)
        except Exception as e:
            response = _handle_exception(e)
        return response

    return inner


def _handle_exception(e):
    if isinstance(e, BaseServerException):
        return e.to_response()
    elif Config.DEBUG_MODE:
        raise e
    else:
        return BaseServerException().to_response()
