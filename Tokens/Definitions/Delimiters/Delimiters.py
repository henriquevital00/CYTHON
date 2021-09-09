from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes


class DelimitersTokens(Enum):

    OPEN_SCOPE = Token('OPEN_SCOPE', TokenTypes.DELIMITER)
    END_SCOPE = Token('END_SCOPE', TokenTypes.DELIMITER)
    END_LINE = Token('END_LINE', TokenTypes.DELIMITER)
    L_PAREN = Token('L_PAREN', TokenTypes.DELIMITER)
    R_PAREN = Token('R_PAREN', TokenTypes.DELIMITER)