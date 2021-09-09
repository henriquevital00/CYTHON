from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class VariableIdentifierTokens(Enum):

    VAR_NAME = Token('VAR_NAME', TokenTypes.IDENTIFIER)