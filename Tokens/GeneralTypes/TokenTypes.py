from enum import Enum
from Tokens.TypesConstants.Delimiters.Delimiters import DelimitersTokens
from Tokens.TypesConstants.Escape.Escape import EscapeCharsTokens
from Tokens.TypesConstants.Literals.Literals import LiteralsTokens
from Tokens.TypesConstants.Operators.Operators import OperatorsTokens
from Tokens.TypesConstants.Statements.Statements import StatementsTokens
from Tokens.TypesConstants.Variables.Variables import VariablesTokens

class TokenTypes:

    DELIMITERS = DelimitersTokens

    ESCAPE_CHARS = EscapeCharsTokens

    LITERALS = LiteralsTokens

    OPERATORS = OperatorsTokens

    STATEMENTS = StatementsTokens

    VARIABLES = VariablesTokens
