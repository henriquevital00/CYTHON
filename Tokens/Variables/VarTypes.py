from enum import Enum
from Tokens.Types import TokenTypes

#                  TOKENS PARA TIPOS DE VARIÁVEIS
# =========================================================================
#   TOKEN         LEXEMA                        SIGNIFICADO
# =========================================================================
#    NUMBER       number         tipo numérico (inteiro ou ponto flutuante)
#    STRING        str           tipo para cadeias de caracteres
#    BOOLEAN       bool          tipo booleano
#
#  TOKEN TYPE: VAR_TYPE
#  REGEX str|number|bool


class VariableTypesTokens(Enum):

    NUMBER = 'number'
    STRING = 'str'
    BOOLEAN = 'bool'

    @property
    def type(cls):
        return TokenTypes.KEYWORD