from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Tokens.Token import Token

class SyntaxTree:
    """
        Class responsible for printing the syntax tree and it's nodes
    """
    root: SyntaxNode

    def __init__(self, root: SyntaxNode):
        self.root = root

    def __str__(self):
        result = []
        self.prettyPrint(self.root, result)
        return ''.join(result)

    def prettyPrint(self, node, result: list, tab: str = '', isLast: bool = True):
        """
            Prints the syntax tree 

            :param node: specific tree node
            :param result: list of nodes
            :param tab: space between the nodes when printing the tree
            :param isLast: verifies if it is the last node

            :return None
        """

        branch = "└──" if isLast else "├──"

        result.append(tab)
        result.append(branch)
        result.append(type(node).__name__)

        if isinstance(node, Token):
            result.append(f" {node.type}: {node.value}")

        tab += "\t" if isLast else "|\t"

        result.append("\n")

        last = node.getChildren()[-1] if len(node.getChildren()) else node

        for child in node.getChildren():
            if isinstance(child, SyntaxNode):
                self.prettyPrint(child, result, tab, last == child)