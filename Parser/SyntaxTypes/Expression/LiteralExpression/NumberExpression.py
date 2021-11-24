from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class NumberExpression(LiteralExpression):
    """
        Class that represents a Number expression
    """
    numberLiteralToken: Token
    """
        Literal token child
    """

    def __init__(self, numberLiteralToken: Token):
        self.numberLiteralToken = numberLiteralToken

    def getChildren(self) -> list:
        """
            Gets the children
        """
        return [self.numberLiteralToken]


