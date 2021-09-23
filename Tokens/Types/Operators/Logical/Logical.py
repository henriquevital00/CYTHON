from enum import Enum

class LogicalOperatorsTokens(Enum):
    """Enum class for Operators tokens"""

    AND = '^&$'
    """ type: AND 

    regex: ^&$ """

    OR = '^\|$'
    """ type: OR 

    regex: ^\|$ """