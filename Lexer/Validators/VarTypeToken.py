from Lexer.Validators.Matcher.TokenMatcher import TokenMatcher
from Tokens.Types.Variables.VarTypes.VarTypes import VariableTypesTokens

def isVariableTypeToken(word):

    typeToken = TokenMatcher.matchToken(tokenEnum=VariableTypesTokens, word=word)

    if typeToken is None:
        return False, None

    return True, typeToken