from Lexer.Validators.General import validators
from Lexer.Exceptions.InvalidTokenException import *

class TokenValidator:

    @staticmethod
    def validateToken(char, word, tokenList):
        for validator in validators:
            token = validator(word)

            if token:
                tokenList.append(token)
                return

        raise InvalidTokenException(f"Invalid token: Unexpected {char}")