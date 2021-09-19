class InvalidTokenException(Exception):

    def __init__(self, message):
        self.message = f"Invalid token: {message}"