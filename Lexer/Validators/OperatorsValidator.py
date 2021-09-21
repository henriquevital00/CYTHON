from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Operators.Arithmetic.Arithmetic import ArithmeticOperationsTokens
from Tokens.Types.Operators.Comparison.Comparison import ComparisonOperatorsTokens


def isOperatorToken(word):

    # ARITHMETIC
    arithmeticToken = TokenMatcher.matchToken(tokenEnum=ArithmeticOperationsTokens, word=word)

    if arithmeticToken is not None:
        return True, arithmeticToken

    # COMPARSION
    comparisonToken = TokenMatcher.matchToken(tokenEnum=ComparisonOperatorsTokens, word=word)

    if comparisonToken is not None:
        return True, comparisonToken

    return False, None