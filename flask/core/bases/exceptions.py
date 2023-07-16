class BaseServerException(Exception):
    status = 500
    detail = "Internal Error."

    def to_response(self):
        return self.detail, self.status


class AuthError(BaseServerException):
    status = 403
    detail = "Invalid credentials."
