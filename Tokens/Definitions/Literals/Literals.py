from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class LiteralsTokens(Enum):

    NUMBER_LITERAL = Token('NUMBER_LITERAL', TokenTypes.LITERALS_TYPES)
    STRING_LITERAL = Token('STRING_LITERAL', TokenTypes.LITERALS_TYPES)
    BOOLEAN_LITERAL = Token('BOOLEAN_LITERAL', TokenTypes.LITERALS_TYPES)