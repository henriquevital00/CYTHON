import re
from Lexer.Validators.Matcher.Matcher import TokenMatcher
from Tokens.Types.Delimiters.Delimiters import DelimitersTokens
from Tokens.Types.Escape.Escape import EscapeCharsTokens
from Tokens.Types.Literals.Literals import LiteralsTokens
from Tokens.Types.Statements.NativeFunctions.NativeFunctions import NativeFunctionsTokens
from Tokens.Types.Operators.Arithmetic.Arithmetic import ArithmeticOperatorsTokens
from Tokens.Types.Operators.Assignment.Assignment import AssignmentOperatorsTokens
from Tokens.Types.Operators.Comparison.Comparison import ComparisonOperatorsTokens
from Tokens.Types.Operators.Logical.Logical import LogicalOperatorsTokens
from Tokens.Types.Statements.Conditionals.Conditionals import ConditionalsTokens
from Tokens.Types.Statements.Loops.Loops import LoopTokens
from Tokens.Types.Variables.Identifier.Identifier import IdentifierToken
from Tokens.Types.Variables.VarTypes.VarTypes import VariableTypesTokens
from Utils.Helpers import removeQuotes
from Utils.Patterns import isFloat

isDelimiterToken = lambda word: TokenMatcher.getToken([DelimitersTokens], word)

isEscapeToken = lambda word: TokenMatcher.getToken([EscapeCharsTokens], word)

isIdentifierToken = lambda word: TokenMatcher.getToken([IdentifierToken], word)

isStatementToken = lambda word: TokenMatcher.getToken([ConditionalsTokens, LoopTokens, NativeFunctionsTokens], word)

isVariableTypeToken = lambda word: TokenMatcher.getToken([VariableTypesTokens], word)

isOperatorToken = lambda word : TokenMatcher.getToken([
        AssignmentOperatorsTokens, ArithmeticOperatorsTokens, ComparisonOperatorsTokens, LogicalOperatorsTokens
], word)

def isLiteralToken(word):
    """
        Return a token instance if the token is a valid literal

        :param word: word to be matched
    """

    literalToken = TokenMatcher.matchToken(tokenEnum=LiteralsTokens, word=word)

    formatters = {
        LiteralsTokens.NUMBER_LITERAL.value: lambda: float(word) if isFloat(word) else int(word),
        LiteralsTokens.STRING_LITERAL.value: lambda: removeQuotes(word),
        LiteralsTokens.BOOLEAN_LITERAL.value: lambda: False if word == "False" else True
    }

    if literalToken:
        for pattern, formatter in formatters.items():
            if re.match(pattern, word):
                literalToken.value = formatter()
                return literalToken
    return None

# ====================================================================================================
# ALL VALIDATORS
validators = \
    [isOperatorToken, isEscapeToken, isDelimiterToken, isVariableTypeToken, isLiteralToken, isStatementToken, isIdentifierToken]