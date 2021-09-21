import re

from Tokens.Token import Token


class TokenMatcher:

    @staticmethod
    def matchToken(tokenEnum, word) -> Token or None:

        for token in tokenEnum:

            tokenType = token.name
            pattern = token.value #regex

            if re.match(pattern, word):
                return Token(tokenType, word)

        return None

