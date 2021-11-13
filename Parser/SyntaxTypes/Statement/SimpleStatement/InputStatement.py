from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Token import Token

class InputStatement(SimpleStatement):
    inputKeyword: Token

    def __init__(self, inputKeyword):
        super().__init__()
        self.inputKeyword = inputKeyword

    def getChildren(self):
        return [self.inputKeyword]
