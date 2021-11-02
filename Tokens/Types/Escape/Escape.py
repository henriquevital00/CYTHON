from enum import Enum


class EscapeCharsTokens(Enum):
    """Enum class for escape chars tokens"""

    WHITESPACE = '^ $'
    """ type: WHITESPACE

    regex: ^ $ """

    NEW_LINE = '^\\n$'
    """ type: NEW LINE

    regex: ^\\n$ """