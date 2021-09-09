from enum import Enum
from Tokens.Types import TokenTypes

#                TOKENS PARA IDENTIFICADORES DE VARIÁVEIS
# ===============================================================
#  Define identificação (nome) das variáveis
#
#  TOKEN TYPE: IDENTIFIER
#  REGEX @([a-z]|[A-Z])+([a-z]|[A-Z]|\d)*
#     começa com @, seguido de pelo menos um caracter alfabético, seguido de qualquer quantidade de caracteres alfanuméricos


class VariableIdentifierTokens(Enum):

    VAR_NAME = "@([a-z]|[A-Z])+([a-z]|[A-Z]|\d)*"

    @property
    def type(cls):
        return TokenTypes.IDENTIFIER