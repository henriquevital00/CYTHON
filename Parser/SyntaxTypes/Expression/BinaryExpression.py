from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class BinaryExpression(Expression):
    """
        Class that represents a Binary expression
    """

    leftTerm: Expression or Token
    """
        Expression left term
    """

    operator: Token
    """
        Expression operator term
    """

    rightTerm: Expression or Token
    """
        Expression right term
    """


    def __init__(self, leftTerm: Expression or Token, operator: Token, rightTerm: Expression or Token):
        self.leftTerm = leftTerm
        self.operator = operator
        self.rightTerm = rightTerm

    def getChildren(self) -> list:
        return [ self.leftTerm, self.operator, self.rightTerm ]