from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Operators.Assignment.Assignment import AssignmentOperatorsTokens


def isAssignmentToken(word):

    assignmentToken = TokenMatcher.matchToken(tokenEnum=AssignmentOperatorsTokens, word=word)

    if assignmentToken is not None:
        return True, assignmentToken

    return False, None