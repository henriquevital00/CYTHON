import re

from Tokens.Token import Token
from Tokens.Types.General import TokenTypes
from Lexer.Validation.Operators import isOperatorToken

class Lexer:


    _tokensList: list[Token] = []


    def validateOperatorsTokens(self, word):


    def validateToken(self, word):

        validators = [
            a,
            b
        ]

        try:

            for validator in validators:

                isValid, Token = validator(word)

                if isValid:
                    self._tokensList.append(Token)
                    return

            raise

        except:
            pass




    def isWhitespace(self, char):
        return char is not None and char.isspace()

    def readChars(self, input):

        resultWord = ''


        for idx, char in enumerate(input):

            isFirstChar = idx == 0
            isSpace = self.isWhitespace(char)
            isDuplicateSpace = self.isWhitespace(input[idx-1])

            if not isSpace:
                resultWord += char

            elif isSpace and isDuplicateSpace and not isFirstChar:
                continue

            self.validateToken(resultWord)


    def readFile(self):

        with open("program.txt", "r") as input:

            self.readChars(input.read())



