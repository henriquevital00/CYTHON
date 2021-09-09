from Tokens.Types import TokenTypes
from enum import Enum

#                         TOKENS DELIMITADORES
# =================================================================================================================================
#      TOKEN             LEXEMA                 SIGNIFICADO
# =================================================================================================================================
#    OPEN_SCOPE            ->        Delimitador de abertura de escopo
#    END_SCOPE            end        Delimitador de final de escopo
#    END_LINE              ;         Delimitador de final de linha
#     L_PAREN              (         Delimitador de prioridade de operações condicionais e de aritmética (abertura de parênteses)
#     R_PAREN              )         Delimitador de prioridade de operações condicionais e de aritmética (fechamento de parênteses)
#
#
#  TOKEN TYPE: DELIMITER
#  REGEX  ->|end|;|(|)
class DelimitersTokens(Enum):

    OPEN_SCOPE = '->'
    END_SCOPE = 'end'
    END_LINE = ';'
    L_PAREN = '('
    R_PAREN = ')'

    @property
    def type(cls):
        return TokenTypes.DELIMITER