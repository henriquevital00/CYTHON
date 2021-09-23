from enum import Enum

class LoopTokens(Enum):
    """Enum class for loop tokens"""

    WHILE = '^while$'
    """
    type: WHILE
    
    regex: ^while$
    """

    FOR   = '^for$'
    """
    type: FOR
    
    regex: ^for$
    """