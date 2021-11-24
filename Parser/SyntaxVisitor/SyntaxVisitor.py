from core import core
from Tokens.Token import Token
from Symbols.Symbol import Symbol
from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Tokens.Constants.TokenConstants import TokenTypes
from Parser.SyntaxTypes.Statement.Statement import Statement
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
from Parser.SyntaxTypes.Statement.SimpleStatement.InputStatement import InputStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.PrintStatement import PrintStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Statement.SimpleStatement.VarAssignSyntax import VarAssignSyntax
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.ElifStatement import ElifStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.ElseStatement import ElseStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.IfStatement import IfStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.WhileStatement import WhileStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.VarDeclareSyntax import VarDeclareSyntax
from Parser.SyntaxTypes.Statement.CompoundStatement.CompoundStatement import CompoundStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement

class SyntaxVisitor:
    """
    This class is responsible for convert the code from cython to python
    """

    def __init__(self, root: SyntaxNode):
        self.root = root

    def getResult(self):
        """
        This method is responsible to convert the traversed tree to python code string

        :return : string
        """
        result = []
        self.visitStatement(self.root, result)
        return ''.join(result)


    def visitExpression(self, node: SyntaxNode):
        """
        This method is responsible for translate cython expression nodes (arithmetic, logical, comparison and literal)
        recursively to python code

        :return : string
        """

        # IS LITERAL LEAF
        if isinstance(node, NumberExpression):
           return str(node.numberLiteralToken.value)

        elif isinstance(node, BooleanExpression):
            return str(node.booleanLiteralToken.value)

        elif isinstance(node, StringExpression):
            return f'"{node.stringLiteralToken.value}"'

        # IS IDENTIFIER LEAF
        if isinstance(node, IdentifierExpression):
            return node.identifierToken.value

        elif isinstance(node, ParenthesizedExpression):
            return f"({self.visitExpression(node.expression)})"

        elif isinstance(node, BinaryExpression):
            leftTerm = self.visitExpression(node.leftTerm)
            rightTerm = self.visitExpression(node.rightTerm)
            operator: Token = node.operator

            if operator.type == TokenTypes.PLUS:
                return f"{leftTerm} + {rightTerm}"

            elif operator.type == TokenTypes.MINUS:
                return f"{leftTerm} - {rightTerm}"

            elif operator.type == TokenTypes.DIVISION:
                return f"{leftTerm} / {rightTerm}"

            elif operator.type == TokenTypes.MULTIPLY:
                return f"{leftTerm} * {rightTerm}"

            elif operator.type == TokenTypes.GREATER:
                return f"{leftTerm} > {rightTerm}"

            elif operator.type == TokenTypes.GREATER_EQUALS:
                return f"{leftTerm} >= {rightTerm}"

            elif operator.type == TokenTypes.LESS:
                return f"{leftTerm} < {rightTerm}"

            elif operator.type == TokenTypes.LESS_EQUALS:
                return f"{leftTerm} <= {rightTerm}"

            elif operator.type == TokenTypes.EQUALS:
                return f"{leftTerm} == {rightTerm}"

            elif operator.type == TokenTypes.DIFFERENT:
                return f"{leftTerm} != {rightTerm}"

            elif operator.type == TokenTypes.AND:
                return f"{leftTerm} and {rightTerm}"

            elif operator.type == TokenTypes.OR:
                return f"{leftTerm} or {rightTerm}"


    def visitVarValue(self, varValue, varType):
        """
        This method is responsible for return the convertion of a cython code  to python code

        :return: string
        """

        if isinstance(varValue, InputStatement):
            if varType == "number":
                return f"float(input())"
            return f"input()"
        else:
            return self.visitExpression(varValue)

    def visitSimpleStatement(self, simpleStmt: SimpleStatement, result):
        """
        This method is responsible for translate cython simple statements (variable assign and declare, inputf and printf) to python code
        """
        if isinstance(simpleStmt, VarAssignSyntax):
            varName = simpleStmt.identifier.value
            varType = simpleStmt.varType.value if simpleStmt.varType else None
            varValue = self.visitVarValue(simpleStmt.value, varType)

            result.append(f"{varName} = {varValue}")

        elif isinstance(simpleStmt, VarDeclareSyntax):
            varName = simpleStmt.identifier.value
            result.append(f"{varName} = None")

        elif isinstance(simpleStmt, InputStatement):
            result.append(f"input()")

        elif isinstance(simpleStmt, PrintStatement):
            valueToPrint = self.visitExpression(simpleStmt.valueToPrint)
            result.append(f"print({valueToPrint})")

    def visitSelectionStatement(self, selectionNode, result, indent):
        """
        This method is responsible for translate cython selection statements (if, elif, else and while) to python code

        :return: None
        """
        keyWord = None
        compoundStmt = selectionNode.scope

        if isinstance(selectionNode, IfStatement):
            keyWord = selectionNode.IfKeyword.value
        elif isinstance(selectionNode, ElifStatement):
            keyWord = selectionNode.ElifKeyword.value
        elif isinstance(selectionNode, ElseStatement):
            keyWord = selectionNode.ElseKeyword.value
        elif isinstance(selectionNode, WhileStatement):
            keyWord = selectionNode.WhileKeyword.value

        if not isinstance(selectionNode, ElseStatement):
            conditions = self.visitExpression(selectionNode.conditions)
            result.append(f"{keyWord} {conditions}:")
        else:
            result.append(f"{keyWord}:")

        self.visitStatement(compoundStmt, result, indent + 1)


    def visitStatement(self, statement: Statement or CompoundStatement, result: list, indent: int = 0):

        """
        This method is responsible for walk global scope tree, translating all nodes to python code

        :return : list
        """
        if not len(statement.getChildren()):
            return result.append('\n' + '\t'*indent + "pass")

        for child in statement.getChildren():

            if child != self.root.getChildren()[0]:
                result.append("\n")

            result.append('\t'*indent)

            if isinstance(child, SelectionStatement):
                self.visitSelectionStatement(child, result, indent)

            elif isinstance(child, SimpleStatement):
                self.visitSimpleStatement(child, result)