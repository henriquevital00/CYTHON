from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class NumberExpression(LiteralExpression):
    numberLiteralToken: Token

    def __init__(self, numberLiteralToken: Token):
        self.numberLiteralToken = numberLiteralToken

    def getChildren(self) -> list:
        return [self.numberLiteralToken]


