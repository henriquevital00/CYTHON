from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
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

    #  IS ARITHMETIC
    arithmeticExpression = SyntaxMatcher.checkSyntax([
        [ArithmeticExpression, self.parseArithmeticTerm],
    ], self)

    if arithmeticExpression:
        return arithmeticExpression

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
    Parser.parseComparisonExpression = parseComparisonExpression
    Parser.parseFinalComparisonExpression = parseFinalComparisonExpression