import re

from Tokens.Token import Token

class Lexer:

    _tokensList: list[Token] = []

    _resultWord: list = []

    _position: int = 0

    _text: str

    _currentChar: str

    def __init__(self, text):
        self._text = text

    def lookAhead(self):
        idx = self._position + 1

        return '\0' if idx >= len(self._text) else self._text[idx]

    def curr_char(self):
        return self._text[self._position]

    def appendToResultWord(self, char):
        self._resultWord.append(char)
        self._position += 1

    def validateToken(self, word):

        validators = [
        # validadores aqui
        ]

        try:

            for validator in validators:

                isValid, Token = validator(word)

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
            self.appendToResultWord(char)

            while self.lookAhead() != '\0':

                if self.lookAhead() == quote:
                    self.appendToResultWord(quote)
                    break

                self.appendToResultWord(self.curr_char())


    def isIdentifier(self, char):

        isLetterOrNumber = lambda c : re.match("^\w$", c)

        if isLetterOrNumber(char):

            self.appendToResultWord(char)

            while self.lookAhead() != '\0':

                if self.isWhitespace(self.lookAhead()):
                    break

                if isLetterOrNumber(self.lookAhead()):
                    self.appendToResultWord(self.curr_char())

    def isWhitespace(self, char):
        return char is not None and char.isspace()

    def readTokens(self):

        resultWord = []

        for char in self._text:

            isFirstChar = self._position == 0
            isSpace = self.isWhitespace(char)
            isDuplicateSpace = self.isWhitespace(input[self._position -1])

            if not isSpace:
                self.appendToResultWord(char)

            elif isSpace and isDuplicateSpace and not isFirstChar:
                self._position += 1
                continue

            self.validateToken(resultWord)

            self._resultWord.clear()

