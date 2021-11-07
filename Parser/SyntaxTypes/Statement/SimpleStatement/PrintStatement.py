from Tokens.Token import Token
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement

class PrintStatement(SimpleStatement):
    printKeyword: Token
    valueToPrint: Expression

    def __init__(self, printKeyword, valueToPrint):
        super().__init__()
        self.printKeyword = printKeyword
        self.valueToPrint = valueToPrint

    def getChildren(self):
        return [self.printKeyword, self.valueToPrint]
