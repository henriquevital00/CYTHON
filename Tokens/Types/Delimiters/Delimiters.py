from enum import Enum

class DelimitersTokens(Enum):

    OPEN_SCOPE = '^{$'
    END_SCOPE = '^}$'
    END_LINE = '^;$'
    L_PAREN = '^($'
    R_PAREN = '^)$'