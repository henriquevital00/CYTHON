from Lexer.Lexer import Lexer
from Tokens.Token import Token
from Tokens.Types.Literals.Literals import LiteralsTokens
from core import core


class Parser:

    def __init__(self):
        self._lexer: Lexer = core.Lexer
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

    # region 1. ARITHMETIC EXPRESSION

    #ARITHMETIC_EXPR -> ARITHMETIC _TERM
                        #| ARITHMETIC_TERM  PLUS ARITHMETIC _EXPR
                        #| ARITHMETIC_TERM  MINUS ARITHMETIC _EXPR

    #ARITHMETIC_TERM ->  ARITHMETIC _FACTOR
                        #| ARITHMETIC _FACTOR MULT ARITHMETIC _TERM
                        #| ARITHMETIC _FACTOR DIVIDE ARITHMETIC _TERM

    #ARITHMETIC_FACTOR -> NUMBER_LITERAL
                        #| IDENTIFIER
                        #| L_PAREN ARITHMETIC _EXPR R_PAREN

    def arithmetic_expr(self):
        result = self.arithmetic_term()

        if not result:
           return 0

        if self.current_token.type == "PLUS":
            self.eat("PLUS")
            return result + self.arithmetic_expr()
        elif self.current_token.type == "MINUS":
            self.eat("MINUS")
            return result - self.arithmetic_expr()

        return result

    def arithmetic_term(self):
        result = self.arithmetic_factor(self.current_token)

        if not result:
           return 1

        if self.current_token.type == "MULTIPLY":
            self.eat("MULTIPLY")
            return result * self.arithmetic_term()
        elif self.current_token.type == "DIVISION":
            self.eat("DIVISION")
            return result / self.arithmetic_term()

        return result

    def arithmetic_factor(self, token):
        if token.type == "NUMBER_LITERAL":
            self.eat("NUMBER_LITERAL")
            return float(token.value)

        elif token.type == "L_PAREN":
            self.eat("L_PAREN")

            expr_result = self.arithmetic_expr()

            if not expr_result:
                pass

            if self.current_token.type == "R_PAREN":
                self.eat("R_PAREN")
                return expr_result

            raise Exception("Faltou parênteses parça")

        return None

    # endregion

    # region 2. LOGIC EXPRESSION





    # LOGICAL_TERM ->   IDENTIFIER
                        # | BOOLEAN_LITERAL
                        # | EXPR

    # LOGICAL_EXPR ->   LOGICAL_EXPR’ OR LOGICAL_EXPR
                        # | LOGICAL_EXPR’
    def logical_expr(self):
        result = self.aux_logical_expr()

        if self.current_token.type == "OR":
            return result or self.logical_expr()

        return result


    # LOGICAL_EXPR’ ->  LOGICAL_TERM AND LOGICAL_TERM
                        # | LOGICAL_TERM
                        # | L_PAREN LOGICAL_EXPR R_PAREN AND LOGICAL_EXPR’
                        # | L_PAREN LOGICAL_EXPR R_PAREN
    def aux_logical_expr(self):
        pass


    # endregion

    def parseGrammar(self):
        print(self.arithmetic_expr())