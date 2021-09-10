from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes


class LogicalOperatorsTokens(Enum):

    AND = Token('AND', TokenTypes.OPERATOR)
    OR = Token('OR', TokenTypes.OPERATOR)
