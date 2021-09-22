from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Operators.Arithmetic.Arithmetic import ArithmeticOperationsTokens
from Tokens.Types.Operators.Assignment.Assignment import AssignmentOperatorsTokens
from Tokens.Types.Operators.Comparison.Comparison import ComparisonOperatorsTokens
from Tokens.Types.Operators.Logical.Logical import LogicalOperatorsTokens

def isOperatorToken(word):
    enums = [AssignmentOperatorsTokens, ArithmeticOperationsTokens, ComparisonOperatorsTokens, LogicalOperatorsTokens]
    return TokenMatcher.hasToken(enums, word)

