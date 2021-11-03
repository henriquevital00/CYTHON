from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Constants.TokenConstants import TokenTypes


# COMPARISON_EXPR -> COMPARISON_TERM COMPARISON_OP COMPARISON_TERM
# COMPARISON_TERM ->  LITERAL
#                    | IDENTIFIER
#                    | ARITHMETIC_EXPR

def parseComparisonExpression(self) -> Expression:
    leftTerm = self.parseFinalComparisonExpression()

    if self.current_token.type in (
            TokenTypes.GREATER,
            TokenTypes.LESS,
            TokenTypes.EQUALS,
            TokenTypes.GREATER_EQUALS,
            TokenTypes.LESS_EQUALS,
            TokenTypes.DIFFERENT
    ):
        operator = self.current_token
        self.eat(operator.type)
        rightTerm = self.parseFinalComparisonExpression()

        return ComparisonExpression(leftTerm, operator, rightTerm)


def parseFinalComparisonExpression(self) -> Expression:
    # IS COMPARISON EXPR PARENTHESIZED
    if self.current_token.type == TokenTypes.L_PAREN:
        left_parenthesis = self.current_token
        self.eat(TokenTypes.L_PAREN)

        expression = self.parseComparisonExpression()

        right_parenthesis = self.current_token
        self.eat(TokenTypes.R_PAREN)

        return ParenthesizedExpression(left_parenthesis, expression, right_parenthesis)

    #  IS ARITHMETIC OR LITERAL EXPRESSION
    expression = SyntaxMatcher.checkSyntax([
        [ArithmeticExpression, self.parseArithmeticTerm],
        [LiteralExpression, self.checkLiteralExpression]
    ], self)

    if expression:
        return expression

def addExtensions():
    Parser.parseComparisonExpression = parseComparisonExpression
    Parser.parseFinalComparisonExpression = parseFinalComparisonExpression