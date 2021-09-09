from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class ComparisonOperatorsTokens(Enum):

    GREATER = Token('GREATER', TokenTypes.OPERATOR)
    LESS = Token('LESS', TokenTypes.OPERATOR)
    EQUALS = Token('EQUALS', TokenTypes.OPERATOR)
    GREATER_EQUALS = Token('GREATER_EQUALS', TokenTypes.OPERATOR)
    LESS_EQUALS = Token('LESS_EQUALS', TokenTypes.OPERATOR)