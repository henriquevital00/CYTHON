from Lexer.Lexer import Lexer
from Parser.SyntaxEvaluator.SyntaxEvaluator import SyntaxEvaluator
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTree.SyntaxTree import SyntaxTree
from Parser.SyntaxTypes.Expression.ArithmeticExpression import ArithmeticExpression
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Parser.SyntaxTypes.Statement.Statement import Statement
from Parser.SyntaxVisitor.SyntaxVisitor import SyntaxVisitor
from Tokens.Constants.TokenConstants import TokenTypes
from Tokens.Token import Token
from core import core


class Parser:
    _lexer: Lexer
    current_token: Token
    _position: int
    _lineCounter: int

    def __init__(self):
        self._lexer: Lexer = core.Lexer
        self.current_token: Token = self._lexer.getNextToken()
        self._position = 0
        self._lineCounter = 1

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
            raise Exception(f"Token {self.current_token.value} not expected")

    def parseStatement(self) -> Statement:
        statementNode = Statement()
        statementChildren = statementNode.children

        while self.current_token.type != TokenTypes.EOF:
            if self.current_token.type == TokenTypes.NEW_LINE:
                self.eat(TokenTypes.NEW_LINE)
                self._lineCounter += 1
                continue

            result = SyntaxMatcher.checkSyntax([
                [SimpleStatement, self.parseSimpleStatement],
                [SelectionStatement, self.parseSelectionStatement],
            ], self)

            if self.current_token.type == TokenTypes.END_COMMAND:
                self.eat(TokenTypes.END_COMMAND)
            else:
                raise Exception(f"Missing ; in end of statement at line {self._lineCounter}")

            statementChildren.append(result)

        print(f"lines: {self._lineCounter}")

        return statementNode

    def parse(self):
        result = self.parseStatement()
        syntaxTree = SyntaxTree(result)
        print(syntaxTree)

        # SyntaxEvaluator.evaluateStatement(syntaxTree.root)
        visitor = SyntaxVisitor(syntaxTree.root).getResult()

        print(visitor)

        with open("teste.py", "w") as file:

            file.write(visitor)