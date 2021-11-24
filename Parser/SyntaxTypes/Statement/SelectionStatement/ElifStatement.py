from Parser.SyntaxTypes.Expression.ConditionalExpression import ConditionalExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Tokens import Token

class ElifStatement(SelectionStatement):
    """
        Class that represents a elif statement
    """

    ElifKeyword: Token
    """
        Elif keyword token
    """


    conditions: ConditionalExpression
    """
        Conditional expression
    """


    def __init__(self, keyword, conditions, scope):
        super().__init__(scope)
        self.ElifKeyword = keyword
        self.conditions = conditions

    def getChildren(self):
        return [self.ElifKeyword, self.conditions, self.scope]