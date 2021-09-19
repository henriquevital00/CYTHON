import re

from Lexer.Exception.InvalidTokenException import InvalidTokenException
from Lexer.Utils.Patterns import isArithmeticOperator, isPoint, isCloseParenthesis, isSeparator, isWhitespace
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

    def appendToResultWord(self, char):
        self._resultWord += char
        self._position += 1

    def clearResultWord(self):
        self._resultWord = ""

    def validateToken(self):

        validators = [
            # validadores aqui
        ]

        try:

            for validator in validators:

                isValid, Token = validator(self._resultWord)

                if isValid:
                    self._tokensList.append(Token)
                    return

            raise ValueError

        except:
            pass

    def isString(self, char):

        isQuote = lambda c: re.match("^\"|'$", c)

        if isQuote(char):

            quote = char
            self.appendToResultWord(quote)

            while True:

                if self.lookAhead() == '\0':
                    if self.curr_char() != quote:
                        raise InvalidTokenException(self._resultWord, f"String f{self.curr_char()} was not closed")

                if self.lookAhead() == quote:
                    self.appendToResultWord(quote)
                    print("STRING", self._resultWord)
                    return True

                self.appendToResultWord(self.curr_char())

        return False


    def isIdentifier(self, char):

        if char.isdigit():
            return False

        isLetterOrNumber = lambda c: re.match("^\w$", c)

        if isLetterOrNumber(char):

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == '\0':
                    if not isLetterOrNumber(self.curr_char()):
                        raise InvalidTokenException(self._resultWord, f"Unexpected '{self.curr_char()}' at")
                    self.appendToResultWord(self.curr_char())
                    print("IDENTIFIER", self._resultWord)
                    return True

                if self.isWhitespace(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())
                    print("IDENTIFIER", self._resultWord)
                    return True

                if isLetterOrNumber(self.lookAhead()) and isLetterOrNumber(self.curr_char()):
                    self.appendToResultWord(self.curr_char())
                else:
                    raise InvalidTokenException(
                        f"{self._resultWord}{self.lookAhead()}",
                        f"Expected letter or number, but {self.lookAhead()} was found , at: "
                    )

        return False

    def isNumber(self, char):

        hasPoint = False

        isValidLookahead =  lambda :\
            isCloseParenthesis(self.lookAhead()) \
            or isSeparator(self.lookAhead()) \
            or isArithmeticOperator(self.lookAhead())

        if char.isdigit():

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == '\0':
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(self._resultWord, "Unexpected '.' at")
                    self.appendToResultWord(self.curr_char())
                    print("NUMBER", float(self._resultWord))
                    return True

                if isPoint(self.lookAhead()):

                    if hasPoint:
                        raise InvalidTokenException(self._resultWord, "Unexpected '.' at")

                    self.appendToResultWord(self.curr_char())

                if self.lookAhead().isdigit():
                    if isPoint(self.curr_char()):
                        hasPoint = True

                    self.appendToResultWord(self.curr_char())

                if isValidLookahead():
                    if isPoint(self.curr_char()):
                        raise InvalidTokenException(self._resultWord, "Expected number but '.' was found at")

                    self.appendToResultWord(self.curr_char())
                    print("NUMBER", float(self._resultWord))
                    return True

        return False

    def handleTokens(self):

        tokenHandlers = [self.isString, self.isIdentifier, self.isNumber]

        for handler in tokenHandlers:

            if handler(self.curr_char()):

                break

    def readInput(self):

        while True:

            if self._position == len(self._text):
                break

            char = self.curr_char()

            if isWhitespace(char):
                self._position += 1
                continue

            self.handleTokens()

            self.clearResultWord()

