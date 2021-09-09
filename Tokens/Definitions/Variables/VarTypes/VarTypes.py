from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class VariableTypesTokens(Enum):

    VAR_NAME = Token('VAR_NAME', TokenTypes.VAR_TYPE)
    NUMBER = Token('NUMBER', TokenTypes.VAR_TYPE)
    STRING = Token('STRING', TokenTypes.VAR_TYPE)
    BOOLEAN = Token('BOOL', TokenTypes.VAR_TYPE)