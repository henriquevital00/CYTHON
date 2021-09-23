from enum import Enum

class EscapeCharsTokens(Enum):
    """Enum class for escape chars tokens"""

    WHITESPACE = '^ $'
    """ type: WHITESPACE
    
    regex: ^ $ """

    NEW_LINE = '^\\n$'
    """ type: WHITESPACE
    
    regex: ^ $ """

    TAB = '^\\t$'
    """ type: TAB
    
    regex: ^\\t$ """