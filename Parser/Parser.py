from Lexer.Lexer import Lexer
from Parser.SyntaxEvaluator.SyntaxEvaluator import SyntaxEvaluator
from Parser.SyntaxTree import SyntaxTree
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.BooleanExpression import BooleanExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.StringExpression import StringExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Parser.SyntaxTypes.Expression.BinaryExpression import BinaryExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
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

    # region 2. LOGIC EXPRESSION

    def parseLogicalTerm(self) -> Expression:
        leftTerm = self.parseLogicalFactor()

        while self.current_token.type == TokenTypes.OR:
            # operator = self.current_token
            # self.eat(operator.type)
            # rightTerm = self.parseLogicalFactor()
            # leftTerm = BinaryExpression(leftTerm, operator, rightTerm)
            pass

        return leftTerm


    def parseLogicalFactor(self) -> Expression:
        pass

    def parseFinalLogicalExpression(self) -> Expression:
        pass

    # endregion

    # region 3. COMPARISON EXPRESSION

    # COMPARISON_EXPR -> COMPARISON_TERM COMPARISON_OP COMPARISON_TERM
    # COMPARISON_TERM ->  LITERAL
    #                    | IDENTIFIER
    #                    | ARITHMETIC_EXPR

    def parseComparisonExpression(self) -> Expression:
        leftTerm = self.parseFinalComparsionExpression()

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
            rightTerm = self.parseFinalComparsionExpression()

            return BinaryExpression(leftTerm, operator, rightTerm)


    def parseFinalComparsionExpression(self) -> Expression:

        # IS COMPARISON EXPR PARENTHESIZED
        if self.current_token.type == TokenTypes.L_PAREN:
            left_parenthesis = self.current_token
            self.eat(TokenTypes.L_PAREN)

            expression = self.parseComparisonExpression()

            right_parenthesis = self.current_token
            self.eat(TokenTypes.R_PAREN)

            return ParenthesizedExpression(left_parenthesis, expression, right_parenthesis)

        oldPosition = self._position
        arithmeticExpression = self.parseArithmeticTerm()
        isArithmetic = isinstance(arithmeticExpression, ArithmeticExpression)


        #  IS ARITHMETIC
        if isArithmetic:
            return arithmeticExpression
        else:
            self.current_token = self._lexer.getNextToken(oldPosition)
            self._position = oldPosition

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

    def parseGrammar(self) -> SyntaxTree:
        result = self.parseComparisonExpression()
        print(SyntaxEvaluator.evaluate(result))
        pass

