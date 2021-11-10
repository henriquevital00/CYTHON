from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.InputStatement import InputStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.PrintStatement import PrintStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from core import core
from Tokens.Token import Token
from Symbols.Symbol import Symbol
from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Tokens.Constants.TokenConstants import TokenTypes
from Parser.SyntaxTypes.Statement.Statement import Statement
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
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


class SyntaxVisitor:

    def __init__(self, root: SyntaxNode):
        self.root = root

    def getResult(self):
        result = []
        self.visitStatement(self.root, result)
        return ''.join(result)


    def visitExpression(self, node: SyntaxNode, string = ''):

        # IS LITERAL LEAF
        if isinstance(node, NumberExpression):
           return str(node.numberLiteralToken.value)

        elif isinstance(node, BooleanExpression):
            return str(node.booleanLiteralToken.value)

        elif isinstance(node, StringExpression):
            return node.stringLiteralToken.value

        # IS IDENTIFIER LEAF
        if isinstance(node, IdentifierExpression):
            return node.identifierToken.value

        elif isinstance(node, ParenthesizedExpression):
            return f"({self.visitExpression(node.expression, string)})"

        elif isinstance(node, BinaryExpression):
            leftTerm = self.visitExpression(node.leftTerm, string)
            rightTerm = self.visitExpression(node.rightTerm, string)
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

    def visitSimpleStatement(self, simpleStmt: SimpleStatement, result):

        if isinstance(simpleStmt, VarAssignSyntax):
            varName = simpleStmt.identifier.value
            varValue = self.visitExpression(simpleStmt.value)

            result.append(f"{varName} = {varValue}")

        elif isinstance(simpleStmt, VarDeclareSyntax):
            varName = simpleStmt.identifier.value
            result.append(f"{varName} = None")

    def visitSelectionStatement(self, selectionNode, result, indent):

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

        conditions = self.visitExpression(selectionNode.conditions)

        result.append(f"{keyWord} {conditions} :")

        self.visitStatement(compoundStmt, result, indent + 1)


    def visitStatement(self, statement, result: list, indent: int = 0):
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



