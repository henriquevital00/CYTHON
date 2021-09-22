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
        idx = self._position + 1
        return 'EOF' if idx >= len(self._text) else self._text[idx]

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
                if self.lookAhead() == 'EOF':

                    # if the last char is not a quote, it's invalid
                    if self.curr_char() != quote:
                        return False

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

        isValidTerminator = lambda c: isSeparator(c) or isEquals(c) or isOpenCurlyBracket(c)

        if isLetterOrNumber(char):

            # if the next char is a valid terminator or is none, just append the current char and return
            if self.lookAhead() == 'EOF' or isValidTerminator(self.lookAhead()):
                self.appendToResultWord(char)
                return True

            self.appendToResultWord(char)

            while True:

                # if it is in the end of the file, the entire identifier/type was read
                if self.lookAhead() == 'EOF':

                    # if the last char is not a letter or number, it's invalid
                    if not isLetterOrNumber(self.curr_char()):
                        return False

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
                    return False

        return False

    def isNumber(self, char):

        hasPoint = False

        isValidTerminator = lambda c: isCloseParenthesis(c) or isSeparator(c) or isOperator(c)

        if char.isdigit():

            self.appendToResultWord(char)

            # if the next char is a valid terminator or is none, just append the current char and return
            if self.lookAhead() == 'EOF' or isValidTerminator(self.lookAhead()):
                return True

            while True:

                # if it is in the end of the file, the entire number was read
                if self.lookAhead() == 'EOF':

                    # if the current char (the last) is not a terminator, it's invalid
                    if not isValidTerminator(self.curr_char()):
                        return False

                    self.appendToResultWord(self.curr_char())
                    return True

                # if the lookahead is a point
                if isPoint(self.lookAhead()):

                    # if already has a point, it's invalid
                    if hasPoint:
                        return False

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
                break

            char = self.curr_char()

            if isWhitespace(char):
                self.advance()
                continue

            self.readTokens()

            TokenValidator.validateToken(self._resultWord, self._tokensList)

            self.clearResultWord()

        # on read finished
        self._tokensList.append(Token("EOF", "eof"))

        prettyTokenPrint = [[token.toString()] for token in self._tokensList]

        for token in prettyTokenPrint:
            print(token)