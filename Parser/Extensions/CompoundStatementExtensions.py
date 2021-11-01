from Parser.Parser import Parser
from Parser.SyntaxMatcher.SyntaxMatcher import SyntaxMatcher
from Parser.SyntaxTypes.Statement.CompoundStatement.CompoundStatement import CompoundStatement
from Parser.SyntaxTypes.Statement.SelectionStatement.SelectionStatement import SelectionStatement
from Parser.SyntaxTypes.Statement.SimpleStatement.SimpleStatement import SimpleStatement
from Tokens.Constants.TokenConstants import TokenTypes

# COMPOUND_STMT -> OPEN_SCOPE CLOSE_SCOPE
#                   | OPEN_SCOPE STATEMENT CLOSE_SCOPE

def parseCompoundStatement(self):
    scope = CompoundStatement()

    if self.current_token.type == TokenTypes.OPEN_SCOPE:
        self.eat(TokenTypes.OPEN_SCOPE)

        while self.current_token.type != TokenTypes.END_SCOPE:
            result = SyntaxMatcher.checkSyntax([
                [SimpleStatement, self.parseSimpleStatement],
                [SelectionStatement, self.parseSelectionStatement],
            ], self)

            scope.children.append(result)

            if self.current_token.type == TokenTypes.END_COMMAND:
                self.eat(TokenTypes.END_COMMAND)
            else:
                raise Exception("Missing ; in end of statement")

            if self.current_token.type == TokenTypes.EOF:
                raise Exception("Missing close scope")

        self.eat(TokenTypes.END_SCOPE)
        return scope

def addExtensions():
    Parser.parseCompoundStatement = parseCompoundStatement