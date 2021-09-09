from enum import Enum
from Tokens.Types import TokenTypes

class ScopeTokens(Enum):

    GLOBAL = "GLOBAL"
    LOCAL = "LOCAL"

    @property
    def type(cls):
        return TokenTypes.SCOPE