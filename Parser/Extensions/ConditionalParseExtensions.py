from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression

# CONDITIONAL_EXPR -> EXPR | LITERAL | IDENTIFIER

def parseConditionalExpression(self) -> Expression:
    #  IS EXPRESSION
    expression = SyntaxMatcher.checkSyntax([
        [LogicalExpression, self.parseLogicalTerm],
        [ComparisonExpression, self.parseComparisonExpression],
        [ArithmeticExpression, self.parseArithmeticTerm],
    ], self)

    if expression:
        return expression

    # IS LITERAL
    literalExpression = self.checkLiteralExpression()

    if literalExpression:
        return literalExpression

def addExtensions():
    Parser.parseConditionalExpression = parseConditionalExpression