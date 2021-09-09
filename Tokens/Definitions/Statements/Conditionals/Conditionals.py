from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class ConditionalTokens(Enum):

    IF = Token('IF', TokenTypes.KEYWORD)
    ELSE = Token('ELSE', TokenTypes.KEYWORD)
    ELIF = Token('ELIF', TokenTypes.KEYWORD)