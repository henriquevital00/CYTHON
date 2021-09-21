from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Statements.Conditionals.Conditionals import ConditionalsTokens


def isStatementToken(word):

    #  CONDITIONALS
    conditionalToken = TokenMatcher.matchToken(tokenEnum=ConditionalsTokens, word=word)

    if conditionalToken is None:
        return False, None

    return True, conditionalToken