from enum import Enum
from Tokens.Types import TokenTypes

#              TOKENS PARA LOOPS
# ==========================================================
#   TOKEN        LEXEMA               SIGNIFICADO
# ==========================================================
#   WHILE         while            Laço de repetição
#
#  TOKEN TYPE: KEYWORD
#  REGEX while
class LoopTokens(Enum):

    WHILE = 'while'

    @property
    def type(cls):
        return TokenTypes.KEYWORD