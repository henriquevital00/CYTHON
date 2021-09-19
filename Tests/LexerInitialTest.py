from Lexer.Lexer import Lexer


class LexerInitialTest:

    def run(self):

        string = input()

        Lexer(string).readInput()