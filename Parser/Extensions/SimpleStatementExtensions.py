from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.VarAssignSyntax import VarAssignSyntax
from Parser.SyntaxTypes.Statement.SimpleStatement.VarDeclareSyntax import VarDeclareSyntax
from Tokens.Constants.TokenConstants import TokenTypes

# SIMPLE_STMT -> ASSIGN | DECLARE
#
# ASSIGN -> VAR_TYPE IDENTIFIER VAR_ASSIGN_OPERATOR (LITERAL | IDENTIFIER | EXPR) ENDCOMMAND
# 	         | IDENTIFIER VAR_ASSIGN_OPERATOR (LITERAL | IDENTIFIER | EXPR) ENDCOMMAND
#
# DECLARE -> VAR_TYPE IDENTIFIER ENDCOMMAND


def parseSimpleStatement(self) -> SimpleStatement:
    var_type = None

    if self.current_token.type in (
            TokenTypes.TYPE_BOOLEAN,
            TokenTypes.TYPE_STRING,
            TokenTypes.TYPE_NUMBER
    ):
        var_type = self.current_token
        self.eat(var_type.type)

    if self.current_token.type == TokenTypes.IDENTIFIER:
        identifier = self.current_token
        self.eat(identifier.type)

        if self.current_token.type == TokenTypes.END_COMMAND and var_type:
            return VarDeclareSyntax(var_type, identifier)

        if self.current_token.type == TokenTypes.VAR_ASSIGN:
            operator = self.current_token
            self.eat(operator.type)

            value = None

            #  IS EXPRESSION
            expression = SyntaxMatcher.checkSyntax([
                [LogicalExpression, self.parseLogicalTerm],
                [ComparisonExpression, self.parseComparisonExpression],
                [ArithmeticExpression, self.parseArithmeticTerm],
            ], self)

            if expression:
                value = expression
            elif self.current_token.type in (
                    TokenTypes.NUMBER_LITERAL,
                    TokenTypes.BOOLEAN_LITERAL,
                    TokenTypes.STRING_LITERAL
            ):
                literalToken = self.current_token
                self.eat(self.current_token.type)

                if literalToken.type == TokenTypes.STRING_LITERAL:
                    value = StringExpression(literalToken)

                elif literalToken.type == TokenTypes.BOOLEAN_LITERAL:
                    value = BooleanExpression(literalToken)

                else:
                    value = NumberExpression(literalToken)

            return VarAssignSyntax(var_type, identifier, operator, value)

def addExtensions():
    Parser.parseSimpleStatement = parseSimpleStatement