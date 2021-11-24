from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.LiteralExpression import LiteralExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression
from Parser.SyntaxTypes.Statement.SimpleStatement.InputStatement import InputStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.PrintStatement import PrintStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.VarAssignSyntax import VarAssignSyntax
from Parser.SyntaxTypes.Statement.SimpleStatement.VarDeclareSyntax import VarDeclareSyntax
from Tokens.Constants.TokenConstants import TokenTypes

# SIMPLE_STMT -> ASSIGN  | DECLARE | PRINT_STMT | INPUT_STMT
#
# PRINT_STMT -> PRINT L_PAREN (IDENTIFIER | LITERAL) R_PAREN
#
# INPUT_STMT -> INPUT L_PAREN R_PAREN
#
# ASSIGN -> VAR_TYPE IDENTIFIER VAR_ASSIGN_OPERATOR (LITERAL | IDENTIFIER | EXPR)
#  	     | IDENTIFIER VAR_ASSIGN_OPERATOR (LITERAL | IDENTIFIER | EXPR)
#
# DECLARE -> VAR_TYPE IDENTIFIER


def parseSimpleStatement(self) -> SimpleStatement:
    """
    Parse a simple statement

    :returns: SimpleStatement
    """
    return self.parseInputOrPrint() or self.parseAssignOrDeclaration()

def parseInputOrPrint(self):
    """
    Parse input and print functions
    """

    # PRINT
    if self.current_token.type == TokenTypes.PRINT:
        printKeywordToken = self.current_token
        self.eat(TokenTypes.PRINT)

        if self.current_token.type == TokenTypes.L_PAREN:
            self.eat(TokenTypes.L_PAREN)

            valueToPrint = SyntaxMatcher.checkSyntax([
                    [IdentifierExpression, self.checkIdentifierExpression],
                    [LiteralExpression, self.checkLiteralExpression],
                ], self)

            if valueToPrint:
                if self.current_token.type == TokenTypes.R_PAREN:
                    self.eat(TokenTypes.R_PAREN)
                    return PrintStatement(printKeywordToken, valueToPrint)
            else:
                raise Exception("Print statement expect 1 argument")

    # INPUT
    if self.current_token.type == TokenTypes.INPUT:
        inputKeywordToken = self.current_token
        self.eat(TokenTypes.INPUT)

        if self.current_token.type == TokenTypes.L_PAREN:
            self.eat(TokenTypes.L_PAREN)

            if self.current_token.type == TokenTypes.R_PAREN:
                self.eat(TokenTypes.R_PAREN)
                return InputStatement(inputKeywordToken)

def parseAssignOrDeclaration(self):
    """
    Parse var assign and declaration statements
    """
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

            #  IS EXPRESSION OR INPUT
            expression = SyntaxMatcher.checkSyntax([
                [InputStatement, self.parseSimpleStatement],
                [LogicalExpression, self.parseLogicalTerm],
                [ComparisonExpression, self.parseComparisonExpression],
                [ArithmeticExpression, self.parseArithmeticTerm],
                [LiteralExpression, self.checkLiteralExpression],
                [IdentifierExpression, self.checkIdentifierExpression],
            ], self)

            if expression:
                value = expression

            return VarAssignSyntax(var_type, identifier, operator, value)

def addExtensions():
    """
        Add the extensions

        :returns: None
    """
    Parser.parseSimpleStatement = parseSimpleStatement
    Parser.parseAssignOrDeclaration = parseAssignOrDeclaration
    Parser.parseInputOrPrint = parseInputOrPrint