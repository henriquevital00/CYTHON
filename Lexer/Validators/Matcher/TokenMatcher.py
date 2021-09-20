import re
from enum import Enum
from typing import Any

from Tokens.Token import Token


class TokenMatcher:

    @staticmethod
    def matchToken(tokenEnum, word, typeCast = str) -> Token or bool:

        for token in tokenEnum:

            tokenType = token.name
            pattern = token.value #regex

            if re.match(pattern, word):

                return Token(tokenType, typeCast(word))

        return None

