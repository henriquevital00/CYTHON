from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes


class LogicalOperatorsTokens(Enum):

    AND = Token('GREATER', TokenTypes.OPERATOR)
    OR = Token('GREATER', TokenTypes.OPERATOR)