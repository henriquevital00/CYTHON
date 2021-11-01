from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class BinaryExpression(Expression):
    leftTerm: Expression
    operator: Token
    rightTerm: Expression

    def __init__(self, leftTerm: Token, operator: Token, rightTerm: Token):
        self.leftTerm = leftTerm
        self.operator = operator
        self.rightTerm = rightTerm

    def getChildren(self) -> list:
        return [ self.leftTerm, self.operator, self.rightTerm ]