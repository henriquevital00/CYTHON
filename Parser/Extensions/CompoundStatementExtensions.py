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

        while True:

            if self.current_token.type == TokenTypes.NEW_LINE:
                self.eat(TokenTypes.NEW_LINE)
                self._lineCounter += 1
                continue

            if self.current_token.type == TokenTypes.END_SCOPE:
                self.eat(TokenTypes.END_SCOPE)
                break

            result = SyntaxMatcher.checkSyntax([
                [SimpleStatement, self.parseSimpleStatement],
                [SelectionStatement, self.parseSelectionStatement],
            ], self)

            scope.children.append(result)

            if self.current_token.type == TokenTypes.END_COMMAND:
                self.eat(TokenTypes.END_COMMAND)
            else:
                raise Exception(f"Missing ; in end of statement at line {self._lineCounter}")

            if self.current_token.type == TokenTypes.EOF:
                raise Exception("Missing close scope")

        return scope

def addExtensions():
    Parser.parseCompoundStatement = parseCompoundStatement