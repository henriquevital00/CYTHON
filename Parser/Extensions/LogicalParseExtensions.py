from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Constants.TokenConstants import TokenTypes

# LOGICAL_EXPR -> LOGICAL_TERM
#                 | LOGICAL_EXPR OR LOGICAL_TERM
# LOGICAL_TERM -> LOGICAL_FACTOR
#                 | LOGICAL_TERM AND LOGICAL_FACTOR
# LOGICAL_FACTOR -> IDENTIFIER
#                   | LITERAL
#                   | EXPR
#                   | L_PAREN EXPR R_PAREN


def parseLogicalTerm(self) -> Expression:
    leftTerm = self.parseLogicalFactor()

    while self.current_token.type in (TokenTypes.OR, TokenTypes.AND):
        operator = self.current_token
        self.eat(operator.type)
        rightTerm = self.parseLogicalFactor()
        leftTerm = LogicalExpression(leftTerm, operator, rightTerm)

    return leftTerm


def parseLogicalFactor(self) -> Expression:
    leftTerm = self.parseFinalLogicalExpression()

    while self.current_token.type == TokenTypes.AND:
        operator = self.current_token
        self.eat(operator.type)

        rightTerm = self.parseFinalLogicalExpression()
        return LogicalExpression(leftTerm, operator, rightTerm)

    return leftTerm


def parseFinalLogicalExpression(self) -> Expression:
    # IS LOGICAL EXPR PARENTHESIZED
    if self.current_token.type == TokenTypes.L_PAREN:
        left_parenthesis = self.current_token
        self.eat(TokenTypes.L_PAREN)

        expression = self.parseLogicalTerm()

        right_parenthesis = self.current_token
        self.eat(TokenTypes.R_PAREN)

        return ParenthesizedExpression(left_parenthesis, expression, right_parenthesis)

    #  IS EXPRESSION
    expression = SyntaxMatcher.checkSyntax([
        [ComparisonExpression, self.parseComparisonExpression],
        [ArithmeticExpression, self.parseArithmeticTerm],
        [LiteralExpression, self.checkLiteralExpression],
        [IdentifierExpression, self.checkIdentifierExpression]
    ], self)

    if expression:
        return expression

def addExtensions():
    Parser.parseLogicalTerm = parseLogicalTerm
    Parser.parseLogicalFactor = parseLogicalFactor
    Parser.parseFinalLogicalExpression = parseFinalLogicalExpression