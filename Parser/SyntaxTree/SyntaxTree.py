from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Tokens.Token import Token

class SyntaxTree:
    root: SyntaxNode

    def __init__(self, root: SyntaxNode):
        self.root = root

    def __str__(self):
        result = []
        self.prettyPrint(self.root, result)
        return ''.join(result)

    def prettyPrint(self, node: SyntaxNode or list, result: list, tab: str = '', isLast: bool = True):

        branch = "└──" if isLast else "├──"

        result.append(tab)
        result.append(branch)
        result.append(type(node).__name__)

        if isinstance(node, Token):
            result.append(f" {node.type}: {node.value}")

        tab += "\t" if isLast else "|\t"

        result.append("\n")

        last = node.getChildren()[-1] if len(node.getChildren()) else node.value

        for child in node.getChildren():
            if isinstance(child, SyntaxNode):
                self.prettyPrint(child, result, tab, last == child)