from Tokens.Types import TokenTypes
from enum import Enum

#               TOKENS PARA OPERADORES DE ATRIBUIÇÃO
# =========================================================================
#   TOKEN           LEXEMA                        SIGNIFICADO
# =========================================================================
#   VAR_ASSIGN        =              operador para atribuição de variáveis
#
#  TOKEN TYPE: OPERATOR
#  REGEX =


class AssignmentOperatorsTokens(Enum):

    VAR_ASSIGN = '='

    @property
    def type(cls):
        return TokenTypes.OPERATOR