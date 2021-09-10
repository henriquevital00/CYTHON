from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class VariableTypesTokens(Enum):

    NUMBER = Token('NUMBER', TokenTypes.VAR_TYPE)
    STRING = Token('STRING', TokenTypes.VAR_TYPE)
    BOOLEAN = Token('BOOL', TokenTypes.VAR_TYPE)
