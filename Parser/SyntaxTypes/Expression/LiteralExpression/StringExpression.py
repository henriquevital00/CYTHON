from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class StringExpression(LiteralExpression):
    """
        Class that represents a String expression
    """

    stringLiteralToken: Token
    """
        Class that represents a Number expression
    """

    def __init__(self, stringLiteralToken: Token):
        self.stringLiteralToken = stringLiteralToken

    def getChildren(self) -> list:
        return [self.stringLiteralToken]


