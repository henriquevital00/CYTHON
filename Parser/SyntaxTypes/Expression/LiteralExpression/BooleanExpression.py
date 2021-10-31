from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class BooleanExpression(LiteralExpression):
    booleanLiteralToken: Token

    def __init__(self, booleanLiteralToken: Token):
        self.booleanLiteralToken = booleanLiteralToken

    def getChildren(self) -> list:
        return [self.booleanLiteralToken]


