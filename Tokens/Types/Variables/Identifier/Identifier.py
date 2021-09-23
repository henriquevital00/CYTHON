from enum import Enum

class IdentifierToken(Enum):
    """Enum class for Operators tokens"""

    IDENTIFIER = '^(([a-z]|[A-Z])|_)+_*(\w|_)*$'
    """ type: IDENTIFIER 

    regex: ^(([a-z]|[A-Z])|_)+_*(\w|_)*$ """

