from Parser.SyntaxNode.SyntaxNode import SyntaxNode

class Statement(SyntaxNode):
    """
        Class that represents a generic statement
    """

    children: list
    """
        All statement children
    """

    def __init__(self):
        self.children = []

    def getChildren(self):
        return self.children