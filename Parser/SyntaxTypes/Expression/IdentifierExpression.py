from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class IdentifierExpression(Expression):
    """
        Class that represents an Identifier expression
    """

    identifierToken: Token
    """
        Identifier token child
    """

    def __init__(self, identifierToken: Token):
        self.identifierToken = identifierToken

    def getChildren(self) -> list:
        return [self.identifierToken]


