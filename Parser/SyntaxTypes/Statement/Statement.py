from Parser.SyntaxNode.SyntaxNode import SyntaxNode

class Statement(SyntaxNode):
    children: list

    def __init__(self):
        self.children = []

    def getChildren(self):
        return self.children