from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Constants.TokenConstants import TokenTypes


# COMPARISON_EXPR -> COMPARISON _TERM  COMPARISON_OP COMPARISON_TERM
# COMPARISON_TERM ->  LITERAL
#                    | IDENTIFIER
#                    | ARITHMETIC_EXPR
#                    | L_PAREN COMPARISON_TERM R_PAREN

def parseComparisonExpression(self) -> ComparisonExpression:
    """
        Parse a comparison expression

        :return: ComparisonExpression
    """
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
    """
        Parse the comparison term leaf

        :return: ComparisonExpression
    """
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
        [LiteralExpression, self.checkLiteralExpression],
        [IdentifierExpression, self.checkIdentifierExpression]
    ], self)

    return expression

def addExtensions() -> None:
    """
        Add the extensions

        :return None
    """
    Parser.parseComparisonExpression = parseComparisonExpression
    Parser.parseFinalComparisonExpression = parseFinalComparisonExpression