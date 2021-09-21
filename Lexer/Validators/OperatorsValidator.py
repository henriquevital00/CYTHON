from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Operators.Arithmetic.Arithmetic import ArithmeticOperationsTokens
from Tokens.Types.Operators.Assignment.Assignment import AssignmentOperatorsTokens
from Tokens.Types.Operators.Comparison.Comparison import ComparisonOperatorsTokens
from Tokens.Types.Operators.Logical.Logical import LogicalOperatorsTokens

def isOperatorToken(word):

    # ASSIGNMENT
    assignmentToken = TokenMatcher.matchToken(tokenEnum=AssignmentOperatorsTokens, word=word)

    if assignmentToken is not None:
        return True, assignmentToken

    # ARITHMETIC
    arithmeticToken = TokenMatcher.matchToken(tokenEnum=ArithmeticOperationsTokens, word=word)

    if arithmeticToken is not None:
        return True, arithmeticToken

    # COMPARSION
    comparisonToken = TokenMatcher.matchToken(tokenEnum=ComparisonOperatorsTokens, word=word)

    if comparisonToken is not None:
        return True, comparisonToken

    # LOGICAL
    logicalToken = TokenMatcher.matchToken(tokenEnum=LogicalOperatorsTokens, word = word)

    if logicalToken is not  None:
        return True, logicalToken

    return False, None

