import core
from Parser.SyntaxNode import SyntaxNode

class SyntaxTree:
    root: SyntaxNode

    def __init__(self, root: SyntaxNode):
        self.root = root