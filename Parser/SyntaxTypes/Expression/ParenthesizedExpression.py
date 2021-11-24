from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class ParenthesizedExpression(Expression):
    """
        Class that represents a parenthesized expression
    """

    leftParenthesis: Token
    """
        Expression left term
    """

    expression: Expression
    """
        Expression term
    """

    rightParenthesis: Token
    """
        Expression right term
    """

    def __init__(self, leftParenthesis: Token, expression: Expression, rightParenthesis: Token):
        self.leftParenthesis = leftParenthesis
        self.expression = expression
        self.rightParenthesis = rightParenthesis

    def getChildren(self) -> list:
        return [ self.leftParenthesis, self.expression, self.rightParenthesis]