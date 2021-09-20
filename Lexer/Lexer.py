from Lexer.Exception.InvalidTokenException import InvalidTokenException
from Lexer.Utils.Patterns import *
from Lexer.Validators.DelimitersTokens import isDelimiterToken
from Lexer.Validators.IdentifierToken import isIdentifierToken
from Lexer.Validators.LiteralsToken import isLiteralToken
from Lexer.Validators.OperatorsToken import isOperatorToken
from Lexer.Validators.VarTypeToken import isVariableTypeToken

from Tokens.Token import Token

class Lexer:

    _tokensList: list[Token] = []

    _resultWord: str = ''

    _position: int = 0

    _text: str

    def __init__(self, text):
        self._text = text

    def lookAhead(self):
        idx = self._position + 1

        return '\0' if idx >= len(self._text) else self._text[idx]

    def curr_char(self):
        return self._text[self._position]

    def advance(self):
        self._position += 1

    def appendToResultWord(self, char):
        self._resultWord += char
        self.advance()

    def clearResultWord(self):
        self._resultWord = ""

    def validateToken(self):

        validators = [
            isDelimiterToken,
            isVariableTypeToken,
            isLiteralToken,
            isIdentifierToken,
            isOperatorToken,
        ]

        for validator in validators:

            isValid, token = validator(self._resultWord or self.curr_char())

            if isValid:
                self._tokensList.append(token.toString())
                print(self._tokensList)
                return

        raise InvalidTokenException(f"Invalid token at {self._resultWord}")

    def isComparisonOperator(self, char):

        # to <=, >=, < and > operators
        if isBiggerOrLessOperator(char):

            #  >= and <=
            if isEquals(self.lookAhead()):
                self.appendToResultWord(char)
                self.appendToResultWord(self.curr_char())
                return True

            # > and <
            self.appendToResultWord(char)
            return True

        # to "==" operator
        if isEquals(char) and isEquals(self.lookAhead()):
            self.appendToResultWord(char)
            self.appendToResultWord(self.curr_char())
            return True

        return False

    def isString(self, char):

        if isQuote(char):

            quote = char
            self.appendToResultWord(quote)

            if isQuote(self.curr_char()):
                self.appendToResultWord(quote)
                return True

            while True:

                # if it is in the end of the file, the entire string was read
                if self.lookAhead() == '\0':

                    # if the last char is not a quote, it's invalid
                    if not isQuote(self.curr_char()):
                        raise InvalidTokenException(f"string {self._resultWord + self.curr_char()} was not closed")

                # if the lookahead is a quote, the entire string was read
                if self.lookAhead() == quote:
                    self.appendToResultWord(self.curr_char())
                    self.appendToResultWord(quote)
                    return True

                # append the current char
                self.appendToResultWord(self.curr_char())

        return False

    def isIdentifierOrType(self, char):

        if char.isdigit():
            return

        isValidTerminator = lambda c: \
            isSeparator(c) \
            or isEquals(c)

        if isLetterOrNumber(char):

            self.appendToResultWord(char)

            if isValidTerminator(self.curr_char()):
                return True

            while True:

                # if it is in the end of the file, the entire identifier/type was read
                if self.lookAhead() == '\0':

                    # if the last char is not a letter or number, it's invalid
                    if not isLetterOrNumber(self.curr_char()):
                        raise InvalidTokenException(f"Unexpected '{self.curr_char()}' at")

                    self.appendToResultWord(self.curr_char())
                    return True

                # if the next char is a separator, the identifier/type was entire read
                if isValidTerminator(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())

                    return True

                # if the next char is '=' character, it is an variable assignment, so it's valid and it was entired read
                if isEquals(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())
                    return True

                if isLetterOrNumber(self.lookAhead()) and isLetterOrNumber(self.curr_char()):
                    self.appendToResultWord(self.curr_char())
                else:
                    raise InvalidTokenException(
                        f"Expected letter or number, but {self.lookAhead()} was found , at: {self._resultWord + self.lookAhead()}"
                    )

        return False

    def isNumber(self, char):

        hasPoint = False

        defaultUnexpectedPointMessage = \
            lambda : f"Expected number but '.' was found at {self._resultWord}{self.curr_char()}{self.lookAhead()}"

        isValidTerminator = lambda c: \
            isCloseParenthesis(c) \
            or isSeparator(c) \
            or isArithmeticOperator(c)

        if char.isdigit():

            if self.lookAhead() == '\0' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == '\0':
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())
                    return True

                if isPoint(self.lookAhead()):

                    if hasPoint:
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())

                elif self.lookAhead().isdigit():
                    if isPoint(self.curr_char()):
                        hasPoint = True

                    self.appendToResultWord(self.curr_char())

                elif isValidTerminator(self.lookAhead()):
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())
                    return True
                else:
                    raise InvalidTokenException("Number cannot be concated with NaN")

        return False

    def handleTokens(self):

        tokenHandlers = [self.isString, self.isComparisonOperator, self.isIdentifierOrType, self.isNumber]

        for handler in tokenHandlers:

            if handler(self.curr_char()):

                return True

    def readInput(self):

        while True:

            if self._position == len(self._text):
                break

            char = self.curr_char()

            if isWhitespace(char):
                self.advance()
                continue

            self.handleTokens()

            self.validateToken()

            self.clearResultWord()