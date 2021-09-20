from enum import Enum

class IdentifierToken(Enum):

    IDENTIFIER = '^(([a-z]|[A-Z])|_)+_*(([a-z]|[A-Z]|\d)|_)*$'

