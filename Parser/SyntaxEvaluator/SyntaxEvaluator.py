from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Constants.TokenConstants import TokenTypes
from Tokens.Token import Token


class SyntaxEvaluator:

    @staticmethod
    def evaluate(node: SyntaxNode):

        if isinstance(node, NumberExpression):
            return float(node.numberLiteralToken.value)

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


