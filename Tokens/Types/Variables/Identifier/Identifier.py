from enum import Enum

class IdentifierToken(Enum):

    IDENTIFIER = '^([a-z]|[A-Z])+([a-z]|[A-Z]|\d)*$'

