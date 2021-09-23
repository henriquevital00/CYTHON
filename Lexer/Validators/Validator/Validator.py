from Lexer.Validators.General import validators
from Lexer.Exceptions.InvalidTokenException import *

class TokenValidator:
    """
    Validates each declared validator
    """

    @staticmethod
    def validateToken(char: str, word: str, tokenList: list) -> None:
        """
            Run each declared validator, returning the token instance if match with word

            :param char: current char
            :param word: result word
            :param tokenList: current token list
            :raise: InvalidTokenException
            :return: None
        """
        for validator in validators:
            token = validator(word)

            if token:
                tokenList.append(token)
                return

        raise InvalidTokenException(f"Invalid token: Unexpected {char}")