from enum import Enum

class ConditionalsTokens(Enum):
    """
    Enum class for conditional tokens
    """

    IF = '^if$'
    """     type: IF 

    regex: ^if$     """

    ELSE = '^else$'
    """     type: ELSE 

    regex: ^else$     """

    ELIF = '^elif$'
    """     type: ELIF 

    regex: ^elif$     """