from Parser.SyntaxNode.SyntaxNode import SyntaxNode
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Token import Token


class SyntaxEvaluator:

    @staticmethod
    def evaluate(node: SyntaxNode):
        if isinstance(node, NumberExpression):
            return float(node.numberLiteralToken.value)

        elif isinstance(node, BooleanExpression):
            return node.booleanLiteralToken.value

        elif isinstance(node, ParenthesizedExpression):
            return SyntaxEvaluator.evaluate(node.expression)

        elif isinstance(node, BinaryExpression):
            leftTerm = SyntaxEvaluator.evaluate(node.leftTerm)
            rightTerm = SyntaxEvaluator.evaluate(node.rightTerm)
            operator: Token = node.operator

            if operator.type == "PLUS":
                return leftTerm + rightTerm
            elif operator.type == "MINUS":
                return leftTerm - rightTerm
            elif operator.type == "DIVISION":
                return leftTerm / rightTerm
            elif operator.type == "MULTIPLY":
                return leftTerm * rightTerm


