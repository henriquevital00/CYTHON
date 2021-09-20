from Lexer.Exception.InvalidTokenException import InvalidTokenException
from Lexer.Utils.Patterns import *
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
            isVariableTypeToken,
            isLiteralToken,
            isIdentifierToken,
            isOperatorToken
        ]

        for validator in validators:

            isValid, token = validator(self._resultWord)

            if isValid:
                self._tokensList.append(token.toString())
                print(self._tokensList)
                return

        raise InvalidTokenException(f"Invalid token at {self._resultWord}")


    def isString(self, char):

        if isQuote(char):

            quote = char
            self.appendToResultWord(quote)

            while True:

                if self.lookAhead() == '\0':
                    if self.curr_char() != quote:
                        raise InvalidTokenException(f"string {self._resultWord + self.curr_char()} was not closed")

                if self.lookAhead() == quote:
                    self.appendToResultWord(self.curr_char())
                    self.appendToResultWord(quote)
                    return True

                self.appendToResultWord(self.curr_char())

        return False

    def isIdentifierOrType(self, char):

        if char.isdigit():
            return False

        if isLetterOrNumber(char):

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == '\0':
                    if not isLetterOrNumber(self.curr_char()):
                        raise InvalidTokenException(f"Unexpected '{self.curr_char()}' at")

                    self.appendToResultWord(self.curr_char())
                    return True

                if isWhitespace(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())

                    return True

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

        isValidLookahead =  lambda :\
            isCloseParenthesis(self.lookAhead()) \
            or isSeparator(self.lookAhead()) \
            or isArithmeticOperator(self.lookAhead())

        if char.isdigit():

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == '\0':
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())
                    return True

                if isNaN(self.lookAhead()) and not isPoint(self.lookAhead()):
                    raise InvalidTokenException("Number cannot be concated with NaN")

                if isPoint(self.lookAhead()):

                    if hasPoint:
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())

                if self.lookAhead().isdigit():
                    if isPoint(self.curr_char()):
                        hasPoint = True

                    self.appendToResultWord(self.curr_char())

                if isValidLookahead():
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(defaultUnexpectedPointMessage())

                    self.appendToResultWord(self.curr_char())
                    return True

        return False

    def handleTokens(self):

        tokenHandlers = [self.isString, self.isIdentifierOrType, self.isNumber]

        for handler in tokenHandlers:

            if handler(self.curr_char()):

                break

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