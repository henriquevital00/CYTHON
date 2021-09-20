from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Operators.Arithmetic.Arithmetic import ArithmeticOperationsTokens

def isOperatorToken(word):

    arithmeticToken = TokenMatcher.matchToken(tokenEnum=ArithmeticOperationsTokens, word=word)

    if arithmeticToken is None:
        return False, None

    return True, arithmeticToken