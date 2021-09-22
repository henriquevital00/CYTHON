from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Statements.Conditionals.Conditionals import ConditionalsTokens

def isStatementToken(word):
    return TokenMatcher.hasToken([ConditionalsTokens], word)