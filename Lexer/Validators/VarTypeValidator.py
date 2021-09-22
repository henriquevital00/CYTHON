from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Variables.VarTypes.VarTypes import VariableTypesTokens

def isVariableTypeToken(word):
    return TokenMatcher.hasToken([VariableTypesTokens], word)