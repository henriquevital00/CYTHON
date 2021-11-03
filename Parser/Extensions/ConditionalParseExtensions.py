from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression import LiteralExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression

# CONDITIONAL_EXPR -> EXPR | LITERAL | IDENTIFIER

def parseConditionalExpression(self) -> Expression:
    expression = SyntaxMatcher.checkSyntax([
        [LogicalExpression, self.parseLogicalTerm],
        [ComparisonExpression, self.parseComparisonExpression],
        [ArithmeticExpression, self.parseArithmeticTerm],
        [LiteralExpression, self.checkLiteralExpression]
    ], self)

    if expression:
        return expression

def addExtensions():
    Parser.parseConditionalExpression = parseConditionalExpression