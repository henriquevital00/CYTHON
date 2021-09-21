from enum import Enum

class EscapeCharsTokens(Enum):

    WHITESPACE = '^ $'
    NEW_LINE = '^\\n$'
    TAB = '^\\t$'