import re

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

        return '\0' if idx >= len(self._text) else self._text[idx-1]

    def curr_char(self):
        return self._text[self._position-1]

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
                    print("STRING")
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
                    print("IDENTIFIER")
                    return True

                if self.isWhitespace(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())
                    print("IDENTIFIER")
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

        isPoint = lambda c : c == "."
        isOperator = lambda c : re.match("^+|-|\*|/$", c)
        isValidLookahead =  \
            lambda : self.lookAhead() == ")" \
                     or self.isSeparator(self.lookAhead()) \
                     or isOperator(self.lookAhead())
        hasPoint = False

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
                    print("NUMBER")
                    return True

        return False

    def isSeparator(self, char):
        return char is not None and re.match("^;|\s|\\n$", char)

    def isWhitespace(self, char):
        return char is not None and char.isspace()

    def readTokens(self):

        while True:

            if self._position == len(self._text):
                break

            char = self._text[self._position]

            # isFirstChar = self._position == 0
            # isSpace = self.isWhitespace(char)
            # isDuplicateSpace = self.isWhitespace(self._text[self._position -1])
            #
            # if not isSpace:
            #     self.appendToResultWord(char)
            #
            # elif isSpace and isDuplicateSpace and not isFirstChar:
            if self.isWhitespace(char) :
                self._position += 1
                continue

            validators = [
                self.isString,
                self.isIdentifier,
                self.isNumber
            ]

            for validator in validators:

                if validator(char):

                    break

            #self.validateToken()

            self.clearResultWord()

