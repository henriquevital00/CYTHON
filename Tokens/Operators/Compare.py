from Tokens.Types import TokenTypes
from enum import Enum

#                TOKENS PARA OPERADORES DE COMPARAÇÃO
# ========================================================================
#      TOKEN             LEXEMA                 SIGNIFICADO
# ========================================================================
#     GREATER              >          operador de comparação MAIOR
#      LESS                <          operador de comparação MENOR
#     EQUALS               ==         operador de comparação IGUAL
#  GREATER_EQUALS          >=         operador de comparação MAIOR OU IGUAL
#   LESS_EQUALS            <=         operador de comparação MENOR OU IGUAL
#
#
#  TOKEN TYPE: OPERATOR
#  REGEX  >|<|>=|<=|==


class CompareOperatorsTokens(Enum):

    GREATER = '>'
    LESS = '<'
    EQUALS = '=='
    GREATER_EQUALS = '>='
    LESS_EQUALS = '<='

    @property
    def type(cls):
        return TokenTypes.OPERATOR