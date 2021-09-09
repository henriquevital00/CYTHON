from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class LoopTokens(Enum):

    WHILE = Token('WHILE', TokenTypes.KEYWORD)