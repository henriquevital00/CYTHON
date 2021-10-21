from Lexer.Lexer import Lexer
from Tokens.Token import Token
from core import core


class Parser:

    def __init__(self):
        self._lexer: Lexer = core.lexer
        self.current_token: Token = self._lexer.getNextToken()

    def eat(self, token_type: str) -> None:
        '''
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception.
        '''

        if self.current_token.type == token_type:
            self.current_token = self._lexer.getNextToken()
        else:
            print("Deu merda Amigao")


    #ARITHMETIC_EXPR -> ARITHMETIC _TERM
    #| ARITHMETIC_TERM  PLUS ARITHMETIC _EXPR
    #| ARITHMETIC_TERM  MINUS ARITHMETIC _EXPR

    #ARITHMETIC_TERM ->  ARITHMETIC _FACTOR
    #| ARITHMETIC _FACTOR MULT ARITHMETIC _TERM
    #| ARITHMETIC _FACTOR DIVIDE ARITHMETIC _TERM

    #ARITHMETIC_FACTOR -> NUMBER_LITERAL
    #| IDENTIFIER
    #| L_PAREN ARITHMETIC _EXPR R_PAREN


    def arithmeticExpr(self):
        result = self.arithmeticTerm()

        while self.current_token.type in ("PLUS", "MINUS"):
            token = self.current_token
            if token.type == "PLUS":
                self.eat("PLUS")
                result = result + self.arithmeticTerm()
            elif token.type == "MINUS":
                self.eat("MINUS")
                result = result - self.arithmeticTerm()

        return result

    def arithmeticTerm(self):
        """term : factor ((MULTIPLY | DIVISION) arithmetic_factor)*"""
        result = self.arithmetic_factor()

        while self.current_token.type in ("MULTIPLY", "DIVISION"):
            token = self.current_token
            if token.type == "MULTIPLY ":
                self.eat("MULTIPLY ")
                result = result * self.arithmetic_factor()
            elif token.type == "DIVISION":
                self.eat("DIVISION")
                result = result / self.arithmetic_factor()

        return result

    def arithmetic_factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value
