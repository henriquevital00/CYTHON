import re
from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Literals.Literals import LiteralsTokens

def isLiteralToken(word):

    # NUMBER
    numberLiteralPattern = LiteralsTokens.NUMBER_LITERAL.value
    isNumberLiteral = re.match(numberLiteralPattern, word)

    if isNumberLiteral:
        isFloat = re.match("^\d+\.\d+$", word)
        cast = float if isFloat else int

        return True, TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word, typeCast=cast)



    # STRING
    stringLiteralPattern = LiteralsTokens.STRING_LITERAL.value
    isStringLiteral = re.match(stringLiteralPattern, word)

    if isStringLiteral:
        return True, TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)



    # BOOLEAN
    booleanLiteralPattern = LiteralsTokens.BOOLEAN_LITERAL.value
    isBooleanLiteral = re.match(booleanLiteralPattern, word)

    if isBooleanLiteral:
        return True, TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word, typeCast=bool)


    return False, None
