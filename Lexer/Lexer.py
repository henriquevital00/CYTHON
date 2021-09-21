from Lexer.Utils.Patterns import *
from Lexer.Validators.AssingmentValidator import isAssignmentToken
from Lexer.Validators.DelimitersValidator import isDelimiterToken
from Lexer.Validators.IdentifierValidator import isIdentifierToken
from Lexer.Validators.LiteralsValidator import isLiteralToken
from Lexer.Validators.OperatorsValidator import isOperatorToken
from Lexer.Validators.VarTypeValidator import isVariableTypeToken
from Lexer.Exception.InvalidTokenException import InvalidTokenException

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
            isAssignmentToken,
            isVariableTypeToken,
            isLiteralToken,
            isIdentifierToken,
            isOperatorToken,
        ]

        for validator in validators:

            isValid, token = validator(self._resultWord)

            if isValid:
                self._tokensList.append(token.toString())
                print(self._tokensList)
                return

        raise InvalidTokenException(f"Invalid token: Unexpected {self._resultWord}")

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

            if self.curr_char() == quote:
                self.appendToResultWord(quote)
                return True

            while True:

                # if it is in the end of the file, the entire string was read
                if self.lookAhead() == '\0':

                    # if the last char is not a quote, it's invalid
                    if self.curr_char() != quote:
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

            # if the next char is a valid terminator or is none, just append the current char and return
            if self.lookAhead() == '\0' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

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
                        f"Expected letter or number, but {self.lookAhead()} was found , at: {self._resultWord + self.curr_char() + self.lookAhead()}"
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

            # if the next char is a valid terminator or is none, just append the current char and return
            if self.lookAhead() == '\0' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

            while True:

                # if it is in the end of the file, the entire number was read
                if self.lookAhead() == '\0':

                    # if the current char (the last) is not a terminator, it's invalid
                    if not isValidTerminator(self.curr_char()):
                        raise InvalidTokenException(f"Unexpected {self.curr_char()} at {self._resultWord + self.curr_char()}")

                    self.appendToResultWord(self.curr_char())
                    return True

                # if the lookahead is a point
                if isPoint(self.lookAhead()):

                    # if already has a point, it's invalid
                    if hasPoint:
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())

                # if the lookhead is a digit
                elif self.lookAhead().isdigit():

                    # if next char is a point, set hasPoint flag
                    if isPoint(self.curr_char()):
                        hasPoint = True

                    self.appendToResultWord(self.curr_char())

                # if the lookahead is a terminator
                elif isValidTerminator(self.lookAhead()):

                    # if the current char (the last) is a point, it's invalid
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

        # if current char has not passed in any handler, just advance the cursos and set result word as the car
        self._resultWord = self.curr_char()
        self.advance()

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