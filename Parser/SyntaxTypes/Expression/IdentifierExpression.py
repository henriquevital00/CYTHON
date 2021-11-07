from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class IdentifierExpression(Expression):
    identifierToken: Token

    def __init__(self, identifierToken: Token):
        self.identifierToken = identifierToken

    def getChildren(self) -> list:
        return [self.identifierToken]


