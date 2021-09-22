from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Delimiters.Delimiters import DelimitersTokens

def isDelimiterToken(word):
    return TokenMatcher.hasToken([DelimitersTokens], word)