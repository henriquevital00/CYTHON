from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression
from Tokens.Constants.TokenConstants import TokenTypes


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
    if self.current_token.type in (
            TokenTypes.NUMBER_LITERAL,
            TokenTypes.BOOLEAN_LITERAL,
            TokenTypes.STRING_LITERAL
    ):
        literalToken = self.current_token
        self.eat(self.current_token.type)

        if literalToken.type == TokenTypes.STRING_LITERAL:
            return StringExpression(literalToken)

        elif literalToken.type == TokenTypes.BOOLEAN_LITERAL:
            return BooleanExpression(literalToken)

        else:
            return NumberExpression(literalToken)

def addExtensions():
    Parser.parseConditionalExpression = parseConditionalExpression