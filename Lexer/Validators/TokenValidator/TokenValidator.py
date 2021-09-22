from Lexer.Exception.InvalidTokenException import InvalidTokenException
from Lexer.Validators.DelimitersValidator import isDelimiterToken
from Lexer.Validators.EscapeValidator import isEscapeToken
from Lexer.Validators.IdentifierValidator import isIdentifierToken
from Lexer.Validators.LiteralsValidator import isLiteralToken
from Lexer.Validators.OperatorsValidator import isOperatorToken
from Lexer.Validators.StatementValidator import isStatementToken
from Lexer.Validators.VarTypeValidator import isVariableTypeToken

class TokenValidator:

    @staticmethod
    def validateToken(word, tokenList):

        validators = [
            isEscapeToken,
            isDelimiterToken,
            isVariableTypeToken,
            isLiteralToken,
            isStatementToken,
            isIdentifierToken,
            isOperatorToken,
        ]

        for validator in validators:

            token = validator(word)

            if token:
                tokenList.append(token)
                return

        raise InvalidTokenException(f"Invalid token: Unexpected {word}")