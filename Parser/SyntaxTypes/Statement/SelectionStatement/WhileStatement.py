from Parser.SyntaxTypes.Expression.ConditionalExpression import ConditionalExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Tokens import Token

class WhileStatement(SelectionStatement):
    """
        Class that represents a while statement
    """

    WhileKeyword: Token
    """
        While keyword token
    """

    conditions: ConditionalExpression
    """
        Conditional expression
    """

    def __init__(self, keyword, conditions, scope):
        super().__init__(scope)
        self.WhileKeyword = keyword
        self.conditions = conditions

    def getChildren(self):
        return [self.WhileKeyword, self.conditions, self.scope]