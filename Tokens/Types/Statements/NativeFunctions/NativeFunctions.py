from enum import Enum


class NativeFunctionsTokens(Enum):
    """
    Enum class for native functions tokens
    """

    PRINT = '^printf$'
    """ type: PRINT 

    regex ^printf$ """

    INPUT = '^inputf$'
    """ type: INPUT 

    regex: ^inputf$ """