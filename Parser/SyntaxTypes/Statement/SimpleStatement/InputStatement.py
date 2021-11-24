from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Token import Token

class InputStatement(SimpleStatement):
    """
        Class that represents an input statement
    """

    inputKeyword: Token
    """
    Input keyword token
    """

    def __init__(self, inputKeyword):
        super().__init__()
        self.inputKeyword = inputKeyword

    def getChildren(self):
        return [self.inputKeyword]
