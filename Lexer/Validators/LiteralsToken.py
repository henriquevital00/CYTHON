import re
from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Literals.Literals import LiteralsTokens

def isLiteralToken(word):

    # NUMBER
    numberLiteralPattern = LiteralsTokens.NUMBER_LITERAL.value
    isNumberLiteral = re.match(numberLiteralPattern, word)

    if isNumberLiteral:
        token = TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)
        isFloat = re.match("^\d+\.\d+$", word)
        word = float(word) if isFloat else int(word)
        token.value = word
        return True, token



    # STRING
    stringLiteralPattern = LiteralsTokens.STRING_LITERAL.value
    isStringLiteral = re.match(stringLiteralPattern, word)

    if isStringLiteral:
        token = TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)
        word = word[1:-1]
        token.value = word
        return True, token



    # BOOLEAN
    booleanLiteralPattern = LiteralsTokens.BOOLEAN_LITERAL.value
    isBooleanLiteral = re.match(booleanLiteralPattern, word)

    if isBooleanLiteral:
        token = TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)
        word = 0 if word == "False" else 1
        token.value = bool(word)
        return True, token


    return False, None
