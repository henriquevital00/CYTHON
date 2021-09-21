from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Delimiters.Delimiters import DelimitersTokens

def isDelimiterToken(word):

    delimiterToken = TokenMatcher.matchToken(tokenEnum=DelimitersTokens, word=word)

    if delimiterToken is None:
        return False, None

    return True, delimiterToken