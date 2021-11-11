from Parser.Parser import Parser
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Parser.SyntaxTypes.Expression.LiteralExpression.NumberExpression import NumberExpression
from Parser.SyntaxTypes.Expression.ParenthesizedExpression import ParenthesizedExpression
from Tokens.Constants.TokenConstants import TokenTypes

# region GRAMMAR
#ARITHMETIC_EXPR -> ARITHMETIC _TERM
#               | ARITHMETIC_EXPR PLUS ARITHMETIC_TERM
#               | ARITHMETIC_EXPR MINUS ARITHMETIC_TERM

#ARITHMETIC_TERM ->  ARITHMETIC_FACTOR
#                   | ARITHMETIC_TERM MULT ARITHMETIC_FACTOR
#                   | ARITHMETIC_TERM DIVIDE ARITHMETIC_FACTOR

#ARITHMETIC_FACTOR -> NUMBER_LITERAL
#                   | IDENTIFIER
#                   | L_PAREN ARITHMETIC_EXPR R_PAREN
# endregion

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

    elif self.current_token.type == TokenTypes.IDENTIFIER:
        identifierToken = self.current_token
        self.eat(TokenTypes.IDENTIFIER)
        return IdentifierExpression(identifierToken)

def addExtensions():
    Parser.parseArithmeticTerm = parseArithmeticTerm
    Parser.parseArithmeticFactor = parseArithmeticFactor
    Parser.parseFinalArithmeticExpression = parseFinalArithmeticExpression
