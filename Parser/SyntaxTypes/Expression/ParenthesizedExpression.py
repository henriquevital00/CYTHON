from Parser.SyntaxTypes.Expression.Expression import Expression
from Tokens import Token

class ParenthesizedExpression(Expression):

    leftParenthesis: Token
    expression: Expression
    rightParenthesis: Token

    def __init__(self, leftParenthesis: Token, expression: Expression, rightParenthesis: Token):
        self.leftParenthesis = leftParenthesis
        self.expression = expression
        self.rightParenthesis = rightParenthesis

    def getChildren(self) -> list:
        return [ self.leftParenthesis, self.expression, self.rightParenthesis]