from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Variables.Identifier.Identifier import IdentifierToken

def isIdentifierToken(word):

    identifierToken = TokenMatcher.matchToken(tokenEnum=IdentifierToken, word=word)

    if identifierToken is None:
        return False, None

    return True, identifierToken