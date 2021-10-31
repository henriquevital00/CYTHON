from Lexer.Lexer import Lexer
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTree import SyntaxTree
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.ComparisonExpression import ComparisonExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.LogicalExpression import LogicalExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.VarAssignSyntax import VarAssignSyntax
from Parser.SyntaxTypes.Statement.SimpleStatement.VarDeclareSyntax import VarDeclareSyntax
from Tokens.Constants.TokenConstants import TokenTypes
from Tokens.Token import Token
from core import core


class Parser:

    _lexer: Lexer
    current_token: Token
    _position: int

    def __init__(self):
        self._lexer: Lexer = core.Lexer
        self.current_token: Token = self._lexer.getNextToken()
        self._position = 0

    def eat(self, token_type: str) -> None:
        '''
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception.
        '''

        if self.current_token.type == token_type:
            self._position += 1
            self.current_token = self._lexer.getNextToken(self._position)
        else:
            print("Deu merda Amigao")

    # region 1. ARITHMETIC EXPRESSION

    #ARITHMETIC_EXPR -> ARITHMETIC _TERM
                        #| ARITHMETIC _EXPR PLUS ARITHMETIC_TERM
                        #| ARITHMETIC _EXPR  MINUS ARITHMETIC_TERM

    #ARITHMETIC_TERM ->  ARITHMETIC _FACTOR
                        #| ARITHMETIC _TERM MULT ARITHMETIC _FACTOR
                        #| ARITHMETIC _TERM DIVIDE ARITHMETIC _FACTOR

    #ARITHMETIC_FACTOR -> NUMBER_LITERAL
                        #| IDENTIFIER
                        #| L_PAREN ARITHMETIC _EXPR R_PAREN

    def parseArithmeticTerm(self) -> Expression:
        leftTerm = self.parseArithmeticFactor()

        while self.current_token.type in (TokenTypes.PLUS, TokenTypes.MINUS):
            operator = self.current_token
            self.eat(operator.type)
            rightTerm = self.parseArithmeticFactor()
            leftTerm = ArithmeticExpression(leftTerm, operator, rightTerm)

        return leftTerm


    def parseArithmeticFactor(self) -> Expression:
        leftTerm = self.parseFinalArithmeticExpression()

        while self.current_token.type in (TokenTypes.MULTIPLY, TokenTypes.DIVISION):
            operator = self.current_token
            self.eat(operator.type)

            rightTerm = self.parseFinalArithmeticExpression()
            leftTerm = ArithmeticExpression(leftTerm, operator, rightTerm)

        return leftTerm

    def parseFinalArithmeticExpression(self) -> Expression:
        if self.current_token.type == TokenTypes.L_PAREN:
            left_parenthesis = self.current_token
            self.eat(TokenTypes.L_PAREN)

            expression = self.parseArithmeticTerm()

            right_parenthesis = self.current_token
            self.eat(TokenTypes.R_PAREN)

            return ParenthesizedExpression(left_parenthesis, expression, right_parenthesis)

        elif self.current_token.type == TokenTypes.NUMBER_LITERAL:
            numberLiteralToken = self.current_token
            self.eat(TokenTypes.NUMBER_LITERAL)
            return NumberExpression(numberLiteralToken)

    # endregion

    # region 2. LOGICAL EXPRESSION

    # LOGICAL_EXPR -> LOGICAL_TERM
    #                 | LOGICAL_EXPR OR LOGICAL_TERM
    #
    #
    # LOGICAL_TERM -> LOGICAL_FACTOR
    #                 | LOGICAL_TERM AND LOGICAL_TERM
    # LOGICAL_FACTOR -> IDENTIFIER
    #                   | LITERAL
    #                   | EXPR
    #                   | L_PAREN LOGICAL_EXPR R_PAREN


    def parseLogicalTerm(self) -> Expression:
        leftTerm = self.parseLogicalFactor()

        while self.current_token.type == TokenTypes.OR:
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

    # endregion

    # region 3. COMPARISON EXPRESSION

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



    # endregion

    # region 4. CONDITIONAL EXPRESSION

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

    # endregion

    # region 5. SIMPLE STATEMENT

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

                if self.current_token == TokenTypes.END_COMMAND:
                    self.eat(TokenTypes.END_COMMAND)

                return VarAssignSyntax(var_type, identifier, operator, value)

    # endregion



    def parseGrammar(self) -> SyntaxTree:
        result = self.parseSimpleStatement()
        pass

