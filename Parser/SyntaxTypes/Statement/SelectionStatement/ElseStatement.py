from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Tokens import Token

class ElseStatement(SelectionStatement):
    ElseKeyword: Token

    def __init__(self, keyword, scope):
        super().__init__(scope)
        self.ElseKeyword = keyword

    def getChildren(self):
        return [self.ElseKeyword, self.scope]