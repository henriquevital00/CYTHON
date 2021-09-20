from enum import Enum

class EscapeCharsTokens(Enum):

    WHITESPACE = '^\s$'
    NEW_LINE = '^\\n$'
    TAB = '\\t'