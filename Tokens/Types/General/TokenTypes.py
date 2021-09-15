from Tokens.Types.Definition.Delimiters.Delimiters import DelimitersTokens
from Tokens.Types.Definition.Escape.Escape import EscapeCharsTokens
from Tokens.Types.Definition.Literals.Literals import LiteralsTokens
from Tokens.Types.Definition.Operators.Operators import OperatorsTokens
from Tokens.Types.Definition.Statements.Statements import StatementsTokens
from Tokens.Types.Definition.Variables.Variables import VariablesTokens

class TokenTypes:

    Operators = OperatorsTokens

    Statements = StatementsTokens

    Variables = VariablesTokens

    Delimiters = DelimitersTokens

    EscapeChars = EscapeCharsTokens

    Literals = LiteralsTokens