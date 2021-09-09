from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class AssignmentOperatorsTokens(Enum):

    VAR_ASSIGN = Token('VAR_ASSIGN', TokenTypes.OPERATOR)