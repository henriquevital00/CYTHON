from Parser.Parser import Parser
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Tokens.Constants.TokenConstants import TokenTypes

# LITERAL_EXPR -> BOOLEAN_LITERAL | NUMBER_LITERAL | STRING_LITERAL

def checkLiteralExpression(self) -> Expression:
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
    Parser.checkLiteralExpression = checkLiteralExpression