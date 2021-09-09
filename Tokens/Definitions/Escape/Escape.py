from enum import Enum
from Tokens.Token import Token
from Tokens.TokenTypes.TokenTypes import TokenTypes

class EscapeCharsTokens(Enum):

    WHITESPACE = Token('WHITESPACE', TokenTypes.ESCAPE_CHARACTER)
    NEW_LINE = Token('NEW_LINE', TokenTypes.ESCAPE_CHARACTER)
    TAB = Token('TAB', TokenTypes.ESCAPE_CHARACTER)
