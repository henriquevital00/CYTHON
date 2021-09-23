from enum import Enum

class LiteralsTokens(Enum):
    """
    Enum class for literal tokens
    """

    NUMBER_LITERAL = '^-?\d+(.\d+)?$'
    """ type: NUMBER_LITERAL 
    
    regex ^-?\d+(.\d+)?$ """

    STRING_LITERAL = """^(".*")|('.*')$"""
    """ type: STRING_LITERAL 
    
    regex: ^(".*")|('.*')$ """

    BOOLEAN_LITERAL = "^True|False$"
    """ type: BOOLEAN_LITERAL 
    
    regex: ^True|False$ """