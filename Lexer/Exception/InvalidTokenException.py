class InvalidTokenException(Exception):

    def __init__(self, word: str, message: str = "Invalid token "):
        self.message = f"{message} '{word}'"