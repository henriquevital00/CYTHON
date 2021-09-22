from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Variables.Identifier.Identifier import IdentifierToken

def isIdentifierToken(word):
    return TokenMatcher.hasToken([IdentifierToken], word)