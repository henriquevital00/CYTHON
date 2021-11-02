from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class BinaryExpression(Expression):
    leftTerm: Expression or Token
    operator: Token
    rightTerm: Expression or Token

    def __init__(self, leftTerm: Expression or Token, operator: Token, rightTerm: Expression or Token):
        self.leftTerm = leftTerm
        self.operator = operator
        self.rightTerm = rightTerm

    def getChildren(self) -> list:
        return [ self.leftTerm, self.operator, self.rightTerm ]