import re

from Tokens.Token import Token


class TokenMatcher:

    @staticmethod
    def hasToken(tokenEnums, word):

        for enum in tokenEnums:

            token = TokenMatcher.matchToken(tokenEnum=enum, word=word)

            if token is not None:
                return token

        return None

    @staticmethod
    def matchToken(tokenEnum, word) -> Token or None:

        for token in tokenEnum:

            tokenType = token.name
            pattern = token.value #regex

            if re.match(pattern, word):
                return Token(tokenType, word)

        return None


