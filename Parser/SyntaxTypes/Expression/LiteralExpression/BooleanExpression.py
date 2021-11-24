from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Tokens import Token

class BooleanExpression(LiteralExpression):
    """
        Class that represents a boolean expression
    """
    
    booleanLiteralToken: Token
    """
        Boolen token child
    """

    def __init__(self, booleanLiteralToken: Token):
        self.booleanLiteralToken = booleanLiteralToken

    def getChildren(self) -> list:
        
        return [self.booleanLiteralToken]


