from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Escape.Escape import EscapeCharsTokens

def isEscapeToken(word):
    return TokenMatcher.hasToken([EscapeCharsTokens], word)