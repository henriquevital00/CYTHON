from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class StringExpression(LiteralExpression):
    stringLiteralToken: Token

    def __init__(self, stringLiteralToken: Token):
        self.stringLiteralToken = stringLiteralToken

    def getChildren(self) -> list:
        return [self.stringLiteralToken]


