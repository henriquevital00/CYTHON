from Tokens.Types import TokenTypes
from enum import Enum

#                    TOKENS PARA CARACTERES DE ESCAPE
# ========================================================================
#      TOKEN             LEXEMA                 SIGNIFICADO
# ========================================================================
#   WHITESPACE             \s         operador de comparação MAIOR
#    NEW_LINE              \n         operador de comparação MENOR
#       TAB                \t         operador de comparação IGUAL
#
#
#  TOKEN TYPE: ESCAPE_CHARACTER
#  REGEX  \s|\n|\t
class EscapeCharsTokens(Enum):

    WHITESPACE = '\s'
    NEW_LINE = '\n'
    TAB = '\t'

    @property
    def type(cls):
        return TokenTypes.ESCAPE_CHARACTER