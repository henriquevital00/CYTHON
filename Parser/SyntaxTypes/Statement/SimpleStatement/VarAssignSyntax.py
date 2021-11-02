from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Token import Token

class VarAssignSyntax(SimpleStatement):
    varType: Token
    identifier: Token
    assignOperator: Token
    value: Expression or Token

    def __init__(self, varType, identifier, assignOperator, value):
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
            children.append(children)

        return children