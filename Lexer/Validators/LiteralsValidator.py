import re
from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Literals.Literals import LiteralsTokens

def isLiteralToken(word):

    literalToken = TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)

    formatters = {}
    formatters[LiteralsTokens.NUMBER_LITERAL.value] = lambda: float(word) if re.match("^\d+\.\d+$", word) else int(word)
    formatters[LiteralsTokens.STRING_LITERAL.value] = lambda: word[1:-1]
    formatters[LiteralsTokens.BOOLEAN_LITERAL.value] = lambda: False if word == "False" else True

    if literalToken:

        for pattern, formatter in formatters.items():

            if re.match(pattern, word):
                literalToken.value = formatter()
                return literalToken
    return None