from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Token import Token

class VarDeclareSyntax(SimpleStatement):
    varType: Token
    identifier: Token

    def __init__(self, varType, identifier):
        super().__init__()
        self.varType = varType
        self.identifier = identifier

    def getChildren(self):
        return [
            self.varType,
            self.identifier
        ]
