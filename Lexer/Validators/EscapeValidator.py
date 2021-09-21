from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Escape.Escape import EscapeCharsTokens

def isEscapeToken(word):

    escapeToken = TokenMatcher.matchToken(tokenEnum=EscapeCharsTokens, word=word)

    if escapeToken is not None:
        return True, escapeToken

    return False, None