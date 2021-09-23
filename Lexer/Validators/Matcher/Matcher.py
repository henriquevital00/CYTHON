import re
from Tokens.Token import Token

class TokenMatcher:
    """Class responsible for validate if the token is correct"""

    @staticmethod
    def getToken(tokenEnums: list, word: str) -> str or None:
        """
            Return a token instance if some token enum in the list is valid

            :param list: list of token enums

            :param word: word to be matched
        """
        for enum in tokenEnums:
            token = TokenMatcher.matchToken(tokenEnum=enum, word=word)

            if token:
                return token

        return None

    @staticmethod
    def matchToken(tokenEnum, word: str) -> Token or None:
        """
            Reads each pattern of token enum and return a Token instance if match

            :param tokenEnum: provided token enum

            :param word: word to be matched

            :return: Token or None
        """
        for token in tokenEnum:
            tokenType = token.name
            pattern = token.value

            if re.match(pattern, word):
                return Token(tokenType, word)

        return None