from Tokens.Types import TokenTypes
from enum import Enum

#                TOKENS PARA OPERADORES LÓGICOS
# =============================================================
#   TOKEN           LEXEMA                SIGNIFICADO
# =============================================================
#    AND               &              operador lógico E
#    OR                |              operador lógico OU
#
#  TOKEN TYPE: OPERATOR
#  REGEX  &|\|


class LogicalOperatorsTokens(Enum):

    AND = '&'
    OR = '|'

    @property
    def type(cls):
        return TokenTypes.OPERATOR