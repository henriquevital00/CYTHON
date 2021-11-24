from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Tokens import Token

class ElseStatement(SelectionStatement):
    """
        Class that represents an else statement
    """

    ElseKeyword: Token
    """
        Else keyword token
    """

    def __init__(self, keyword, scope):
        super().__init__(scope)
        self.ElseKeyword = keyword

    def getChildren(self):
        return [self.ElseKeyword, self.scope]