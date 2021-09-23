from enum import Enum

class ArithmeticOperatorsTokens(Enum):
    """Enum class for Operators tokens"""

    PLUS = '^\+$'
    """ type: PLUS 

    regex: ^\+$ """

    MINUS = '^-$'
    """ type: MINUS 

    regex: ^-$ """

    DIVISION = '^/$'
    """ type: DIVISION 

    regex: ^/$ """

    MULTIPLY = '^\*$'
    """ type: DIVISION 

    regex: ^\*$ """
