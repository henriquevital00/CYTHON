from Tokens.Types import TokenTypes
from enum import Enum

#                TOKENS PARA OPERAÇÕES ARITMÉTICAS
# =============================================================
#   TOKEN           LEXEMA                SIGNIFICADO
# =============================================================
#    PLUS             +             operação de adição
#   MINUS             -             operação de subtração
#   DIVIDE            /             operação de divisão 
#   MULTIPLY          *             operação de multiplicação
#
#  REGEX  ^+|-|/|*^

class ArithmeticOperationsTokens(Enum):

    PLUS = '+'
    MINUS = '-'
    DIVIDE = '/'
    MULTIPLY = '*'  

    @property
    def type(cls):
        return TokenTypes.OPERATOR