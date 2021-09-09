from Tokens.Types import TokenTypes
from enum import Enum

#                  TOKENS PARA LITERAIS
# ===================================================================================================
#   TOKEN                   LEXEMA                        SIGNIFICADO
# ===================================================================================================
#    NUMBER_LITERAL       \d+(.\d+)?              Literais para constantes numericas
#    STRING_LITERAL       ('\w*')|("\w*")         Literais para constantes de sequencia de caracter
#    BOOLEAN_LITERAL      '0|1|True|False         Literais para constantes booleanas
#
#  TOKEN TYPE: LITERALS_CONSTANTS
#  number_literal = \d+(.\d+)?
#  string_literal = ('\w*')|("\w*")
#  boolean_literal = 0|1|True|False


class LiteralsTokens(Enum):

    NUMBER_LITERAL = '\d+(.\d+)?'
    STRING_LITERAL = '''('\w*')|("\w*")'''
    BOOLEAN_LITERAL = '0|1|True|False'

    @property
    def type(cls):
        return TokenTypes.LITERALS_TYPES