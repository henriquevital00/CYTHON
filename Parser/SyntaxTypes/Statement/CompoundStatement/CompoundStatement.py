from Parser.SyntaxTypes.Statement.Statement import Statement

class CompoundStatement(Statement):
    children: list

    def __init__(self):
        self.children = []

    def getChildren(self):
        return self.children