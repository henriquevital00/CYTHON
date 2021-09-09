from Tokens.Types import TokenTypes
from enum import Enum

#              TOKENS PARA STATEMENTS CONDICIONAIS
# ==========================================================
#   TOKEN        LEXEMA               SIGNIFICADO
# ==========================================================
#    IF              if         condição inicial
#   ELIF            elif        condição intermediária/final
#   ELSE            else        condição final
#
#  TOKEN TYPE: KEYWORD
#  REGEX if|else|elif


class ConditionalTokens(Enum):

    IF = 'if'
    ELSE = 'else'
    ELIF = "elif"

    @property
    def type(cls):
        return TokenTypes.KEYWORD