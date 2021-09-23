from enum import Enum


class ComparisonOperatorsTokens(Enum):
    """Enum class for comparison operators tokens"""

    GREATER = '^>$'
    """
    type: GREATER
    
    regex: ^>$
    """

    LESS = '^<$'
    """
    type: LESS

    regex: ^<$
    """

    EQUALS = '^==$'
    """
    type: EQUALS

    regex: ^==$
    """

    GREATER_EQUALS = '^>=$'
    """
    type: GREATER_EQUALS

    regex: ^>=$
    """

    LESS_EQUALS = '^<=$'
    """
    type: LESS_EQUALS

    regex: ^<=$
    """

    DIFFERENT = '^!=$'
    """
    type: DIFFERENT

    regex: ^!=$
    """
