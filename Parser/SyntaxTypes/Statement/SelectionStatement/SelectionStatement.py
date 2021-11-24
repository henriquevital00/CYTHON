from Parser.SyntaxTypes.Statement.CompoundStatement.CompoundStatement import CompoundStatement
from Parser.SyntaxTypes.Statement.Statement import Statement

class SelectionStatement(Statement):
    """
        Class that represents a selection statement
    """

    scope: CompoundStatement
    """
        Statement scope
    """

    def __init__(self, scope):
        super().__init__()
        self.scope = scope