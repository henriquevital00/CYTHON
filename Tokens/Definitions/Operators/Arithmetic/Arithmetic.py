from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class ArithmeticOperationsTokens(Enum):

    PLUS = Token('PLUS', TokenTypes.OPERATOR)
    MINUS = Token('MINUS', TokenTypes.OPERATOR)
    DIVISION = Token('DIVISION', TokenTypes.OPERATOR)
    MULTIPLY = Token('MULTIPLY', TokenTypes.OPERATOR)
