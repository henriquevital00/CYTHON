from Parser.SyntaxTypes.Expression.ConditionalExpression import ConditionalExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Tokens import Token

class IfStatement(SelectionStatement):
    IfKeyword: Token
    conditions: ConditionalExpression

    def __init__(self, keyword, conditions, scope):
        super().__init__(scope)
        self.IfKeyword = keyword
        self.conditions = conditions

    def getChildren(self):
        return [self.IfKeyword, self.conditions, self.scope]