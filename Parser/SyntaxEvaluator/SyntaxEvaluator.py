from Parser.SyntaxTypes.Statement.SimpleStatement.InputStatement import InputStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.PrintStatement import PrintStatement
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

class SyntaxEvaluator:

    @staticmethod
    def evaluateExpression(node: SyntaxNode):

        # IS LITERAL LEAF
        if isinstance(node, NumberExpression):
            return node.numberLiteralToken.value

        elif isinstance(node, BooleanExpression):
            return node.booleanLiteralToken.value

        elif isinstance(node, StringExpression):
            return node.stringLiteralToken.value

        # IS IDENTIFIER LEAF
        if isinstance(node, IdentifierExpression):
            varSymbol = core.SymbolsTable.findSymbolByKey(node.identifierToken.value)
            return varSymbol.value

        elif isinstance(node, ParenthesizedExpression):
            return SyntaxEvaluator.evaluateExpression(node.expression)

        elif isinstance(node, BinaryExpression):
            leftTerm = SyntaxEvaluator.evaluateExpression(node.leftTerm)
            rightTerm = SyntaxEvaluator.evaluateExpression(node.rightTerm)
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
    def evaluateStatement(statement: Statement):
        stmtIdx = 0

        while stmtIdx < len(statement.getChildren()):
            stmt = statement.getChildren()[stmtIdx]

            numberOfConditionalStmt = SyntaxEvaluator.appendConditionalSyntax(stmt, statement, stmtIdx)

            if numberOfConditionalStmt > 0:
                stmtIdx += numberOfConditionalStmt
                continue

            elif isinstance(stmt, WhileStatement):
                SyntaxEvaluator.evaluateWhileStatement(stmt)

            elif isinstance(stmt, VarDeclareSyntax):
                SyntaxEvaluator.evaluateVarDeclareStatement(stmt)

            elif isinstance(stmt, VarAssignSyntax):
                SyntaxEvaluator.evaluateVarAssignStatement(stmt)

            elif isinstance(stmt, PrintStatement):
                SyntaxEvaluator.evaluatePrintStatement(stmt)

            stmtIdx += 1

    @staticmethod
    def evaluatePrintStatement(printStatement):
        valueToPrint = SyntaxEvaluator.evaluateExpression(printStatement.valueToPrint)
        print(valueToPrint)

    @staticmethod
    def evaluateVarAssignStatement(assignStmt: VarAssignSyntax):
        varType = assignStmt.varType
        varName = assignStmt.identifier.value
        varValue = SyntaxEvaluator.evaluateVarValue(assignStmt.value)
        availableTypes = {
            "number": [float, int],
            "str": [str],
            "bool": [bool]
        }

        if varType:
            varType = varType.value
            assignType = None

            for typeKey, v in availableTypes.items():
                for typeValue in v:
                    if type(varValue) == typeValue:
                        assignType = typeKey
                        break

            if assignType != varType:
                raise Exception(f"Type {varType} cannot be assigned to {assignType}")

            varSymbol = Symbol(varType, varName, varValue)
            core.SymbolsTable.storeSymbol(varSymbol)
        else:
            symbolType = core.SymbolsTable.findSymbolByKey(varName).type
            assignType = None

            for typeKey, v in availableTypes.items():
                for typeValue in v:
                    if type(varValue) == typeValue:
                        assignType = typeKey
                        break

            if assignType != symbolType:
                raise Exception(f"Type {symbolType} cannot be assigned to {assignType}")

            core.SymbolsTable.updateSymbol(varName, varValue)

    @staticmethod
    def evaluateVarDeclareStatement(declareStmt: VarDeclareSyntax):
        varType = declareStmt.varType.value
        varName = declareStmt.identifier.value

        varSymbol = Symbol(varType, varName, None)
        core.SymbolsTable.storeSymbol(varSymbol)

    @staticmethod
    def evaluateWhileStatement(whileStmt: WhileStatement):
        while SyntaxEvaluator.evaluateExpression(whileStmt.conditions):
            SyntaxEvaluator.evaluateStatement(whileStmt.scope)

    @staticmethod
    def evaluateConditionalStatement(conditionalNodes):
        ifStmt = conditionalNodes[0]

        if SyntaxEvaluator.evaluateExpression(ifStmt.conditions):
            SyntaxEvaluator.evaluateStatement(ifStmt.scope)
            return

        elif len(conditionalNodes) > 1:
            nodeIdx = 1
            while isinstance(conditionalNodes[nodeIdx], ElifStatement):
                elifStmt = conditionalNodes[nodeIdx]

                if SyntaxEvaluator.evaluateExpression(elifStmt.conditions):
                    SyntaxEvaluator.evaluateStatement(elifStmt.scope)
                    return

                nodeIdx += 1

            if isinstance(conditionalNodes[nodeIdx], ElseStatement):
                elseStmt = conditionalNodes[nodeIdx]
                SyntaxEvaluator.evaluateStatement(elseStmt.scope)
                return

    @staticmethod
    def appendConditionalSyntax(node, statement, idx):
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

                if isinstance(statement.getChildren()[nextIdx], ElseStatement):
                    conditionalsStatements.append(statement.getChildren()[nextIdx])

            SyntaxEvaluator.evaluateConditionalStatement(conditionalsStatements)

        return len(conditionalsStatements)

    @staticmethod
    def evaluateVarValue(varValue):
        if isinstance(varValue, InputStatement):
            inputValue = input()
            try:
                return float(inputValue)
            except:
                return inputValue

        return SyntaxEvaluator.evaluateExpression(varValue)
