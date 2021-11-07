from enum import Enum


class NativeFunctionsTokens(Enum):
    """
    Enum class for native functions tokens
    """

    PRINT = '^print?$'
    """ type: PRINT 

    regex ^print?$ """

    INPUT = '^input$'
    """ type: INPUT 

    regex: ^input$ """