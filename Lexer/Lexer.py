from Lexer.Utils.Patterns import *
from Lexer.Validators.TokenValidator.TokenValidator import TokenValidator
from Tokens.Token import Token

class Lexer:
    _tokensList: list = []
    _resultWord: str = ''
    _position: int = 0
    _text: str

    def __init__(self, text):
        self._text = text

    def lookAhead(self):
        next = self._position + 1
        return 'EOF' if next >= len(self._text) else self._text[next]

    def curr_char(self):
        return self._text[self._position]

    def advance(self):
        self._position += 1

    def appendToResultWord(self, char):
        self._resultWord += char
        self.advance()

    def clearResultWord(self):
        self._resultWord = ""

    def isComparisonOperator(self, char):
        if isComparisonStarter(char):
            if isEquals(self.lookAhead()):
                self.appendToResultWord(char)
                self.appendToResultWord(self.curr_char())
                return True

            self.appendToResultWord(char)
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

                if self.lookAhead() == 'EOF':
                    if self.curr_char() != quote:
                        return False

                elif self.lookAhead() == quote:
                    self.appendToResultWord(self.curr_char())
                    self.appendToResultWord(quote)
                    return True

                self.appendToResultWord(self.curr_char())

        return False

    def isIdentifierOrType(self, char):
        if isLetter(char) or isUnderscore(char):

            isValidTerminator = lambda c: isSeparator(c) or isOperator(c) or isOpener(c) or isEquals(c)

            if self.lookAhead() == 'EOF' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == 'EOF' or isValidTerminator(self.lookAhead()):
                    if not (isLetterOrNumber(self.curr_char()) or isUnderscore(self.curr_char())):
                        return False

                    self.appendToResultWord(self.curr_char())
                    return True

                if isLetterOrNumber(self.curr_char()) or isUnderscore(char):
                    self.appendToResultWord(self.curr_char())
                else:
                    return False

        return False

    def isNumber(self, char):
        if char.isdigit() or isMinus(char):
            hasPoint = False
            isValidTerminator = lambda c: isCloseParenthesis(c) or isSeparator(c) or isOperator(c)

            if self.lookAhead() == 'EOF' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

            while True:

                if self.lookAhead() == 'EOF':
                    if not isValidTerminator(self.curr_char()):
                        return False

                    self.appendToResultWord(self.curr_char())
                    return True

                elif isPoint(self.lookAhead()):
                    if hasPoint:
                        return False

                    self.appendToResultWord(self.curr_char())

                elif self.lookAhead().isdigit():
                    if isPoint(self.curr_char()):
                        hasPoint = True

                    self.appendToResultWord(self.curr_char())

                elif isValidTerminator(self.lookAhead()):
                    if isPoint(self.curr_char()):
                        return False

                    self.appendToResultWord(self.curr_char())
                    return True
                else:
                    return False

        return False

    def readTokens(self):
        readers = [self.isString, self.isComparisonOperator, self.isIdentifierOrType, self.isNumber]

        for reader in readers:
            if reader(self.curr_char()):
                return

        # if current char has not passed in any handler, just advance and set result word as the char
        self._resultWord = self.curr_char()
        self.advance()

    def readInput(self):
        while True:
            if self._position == len(self._text):
                self._tokensList.append(Token("EOF", "eof"))
                break

            char = self.curr_char()

            if isWhitespace(char):
                self.advance()
                continue

            self.readTokens()

            TokenValidator.validateToken(char, self._resultWord, self._tokensList)

            self.clearResultWord()

        prettyTokenPrint = [[token.toString()] for token in self._tokensList]

        for token in prettyTokenPrint:
            print(token)