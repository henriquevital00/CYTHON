from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class ScopeTokens(Enum):

    GLOBAL = Token("GLOBAL", TokenTypes.SCOPE)
    LOCAL = Token("LOCAL", TokenTypes.SCOPE)