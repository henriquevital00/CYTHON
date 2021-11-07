from Parser.Parser import Parser
from Parser.SyntaxTypes.Expression.Expression import Expression
from Parser.SyntaxTypes.Expression.IdentifierExpression import IdentifierExpression
from Tokens.Constants.TokenConstants import TokenTypes

def checkIdentifierExpression(self) -> Expression:
    if self.current_token.type == TokenTypes.IDENTIFIER:
        identifierToken = self.current_token
        self.eat(self.current_token.type)

        return IdentifierExpression(identifierToken)

def addExtensions():
    Parser.checkIdentifierExpression = checkIdentifierExpression