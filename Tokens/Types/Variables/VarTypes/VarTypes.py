from enum import Enum

class VariableTypesTokens(Enum):
    """Enum class for Variables Types tokens"""

    TYPE_NUMBER = '^number$'
    """ type: TYPE_NUMBER

    regex: ^number$ """

    TYPE_STRING = '^str$'
    """ type: TYPE_STRING

    regex: ^str$ """

    TYPE_BOOLEAN = '^bool$'
    """ type: TYPE_BOOLEAN

    regex: ^bool$ """
