from Tokens.Token import Token
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement

class PrintStatement(SimpleStatement):
    """
        Class that represents a print statement
    """

    printKeyword: Token
    """
        Print keyword token
    """

    valueToPrint: Expression
    """
        Expression value to print
    """

    def __init__(self, printKeyword, valueToPrint):
        super().__init__()
        self.printKeyword = printKeyword
        self.valueToPrint = valueToPrint

    def getChildren(self):
        return [self.printKeyword, self.valueToPrint]
