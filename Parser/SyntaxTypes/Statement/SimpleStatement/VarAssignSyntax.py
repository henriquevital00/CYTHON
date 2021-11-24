from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Token import Token

class VarAssignSyntax(SimpleStatement):
    """
        Class that represents a var assign syntax
    """

    varType: Token
    """
        Variable type keyword token
    """

    identifier: Token
    """
        Identifier token
    """

    assignOperator: Token
    """
        Assign operator token
    """

    value: Expression or Token
    """
        Variable value
    """

    def __init__(self, varType, identifier, assignOperator, value):
        super().__init__()
        self.varType = varType
        self.identifier = identifier
        self.assignOperator = assignOperator
        self.value = value

    def getChildren(self):
        children = [
            self.identifier,
            self.assignOperator,
            self.value
        ]

        if self.varType:
            children.append(self.varType)

        return children
