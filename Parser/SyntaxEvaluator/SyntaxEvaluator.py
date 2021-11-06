from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.ElifStatement import ElifStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.ElseStatement import ElseStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.IfStatement import IfStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.WhileStatement import WhileStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.VarDeclareSyntax import VarDeclareSyntax
from Parser.SyntaxTypes.Statement.Statement import Statement
from Tokens.Constants.TokenConstants import TokenTypes
from Tokens.Token import Token


class SyntaxEvaluator:

    @staticmethod
    def evaluate(node: SyntaxNode):

        if isinstance(node, NumberExpression):
            return node.numberLiteralToken.value

        elif isinstance(node, BooleanExpression):
            return node.booleanLiteralToken.value

        elif isinstance(node, StringExpression):
            return node.stringLiteralToken.value


        elif isinstance(node, ParenthesizedExpression):
            return SyntaxEvaluator.evaluate(node.expression)

        elif isinstance(node, BinaryExpression):
            leftTerm = SyntaxEvaluator.evaluate(node.leftTerm)
            rightTerm = SyntaxEvaluator.evaluate(node.rightTerm)
            operator: Token = node.operator

            if operator.type == TokenTypes.PLUS:
                return leftTerm + rightTerm
            elif operator.type == TokenTypes.MINUS:
                return leftTerm - rightTerm
            elif operator.type == TokenTypes.DIVISION:
                return leftTerm / rightTerm
            elif operator.type == TokenTypes.MULTIPLY:
                return leftTerm * rightTerm

            elif operator.type == TokenTypes.GREATER:
                return leftTerm > rightTerm
            elif operator.type == TokenTypes.GREATER_EQUALS:
                return leftTerm >= rightTerm
            elif operator.type == TokenTypes.LESS:
                return leftTerm < rightTerm
            elif operator.type == TokenTypes.LESS_EQUALS:
                return leftTerm <= rightTerm
            elif operator.type == TokenTypes.EQUALS:
                return leftTerm == rightTerm
            elif operator.type == TokenTypes.DIFFERENT:
                return leftTerm != rightTerm

            elif operator.type == TokenTypes.AND:
                return leftTerm and rightTerm
            elif operator.type == TokenTypes.OR:
                return leftTerm or rightTerm

    @staticmethod
    def evaluateIfStatement(conditionalNodes):
        ifStmt = conditionalNodes[0]

        if SyntaxEvaluator.evaluate(ifStmt.conditions):
            print("entrou no if")
            SyntaxEvaluator.evaluateStatement(ifStmt.scope)
            return

        elif len(conditionalNodes) > 1:
            nodeIdx = 1
            while isinstance(conditionalNodes[nodeIdx], ElifStatement):
                elifStmt = conditionalNodes[nodeIdx]

                if SyntaxEvaluator.evaluate(elifStmt.conditions):
                    print(f"entrou no elif {nodeIdx}")
                    SyntaxEvaluator.evaluateStatement(elifStmt.scope)
                    return

                nodeIdx += 1

            if isinstance(conditionalNodes[nodeIdx], ElseStatement):
                elseStmt = conditionalNodes[nodeIdx]
                print(f"entrou no else")
                SyntaxEvaluator.evaluateStatement(elseStmt.scope)

                return


    @staticmethod
    def evaluateStatement(statement: Statement):

        stmtIdx = 0
        while stmtIdx < len(statement.getChildren()):
            node = statement.getChildren()[stmtIdx]

            numberOfConditionalStmt = SyntaxEvaluator.appendConditionalsSyntax(node, statement, stmtIdx)

            if numberOfConditionalStmt > 0:
                stmtIdx += numberOfConditionalStmt
                continue

            elif isinstance(node, VarDeclareSyntax):
                pass

            stmtIdx += 1

    @staticmethod
    def appendConditionalsSyntax(node, statement, idx):
        conditionalsStatements = []

        if isinstance(node, IfStatement):
            conditionalsStatements.append(node)

            nextIdx = idx + 1

            if nextIdx < len(statement.getChildren()):
                while isinstance(statement.getChildren()[nextIdx], ElifStatement):
                    conditionalsStatements.append(statement.getChildren()[nextIdx])
                    if len(statement.getChildren()) > nextIdx + 1:
                        nextIdx += 1
                    else:
                        break

                while isinstance(statement.getChildren()[nextIdx], ElseStatement):
                    conditionalsStatements.append(statement.getChildren()[nextIdx])
                    if len(statement.getChildren()) > nextIdx + 1:
                        nextIdx += 1
                    else:
                        break

            SyntaxEvaluator.evaluateIfStatement(conditionalsStatements)

        return len(conditionalsStatements)