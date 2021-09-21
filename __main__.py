from Lexer.Lexer import Lexer
import re
from Tests.LexerInitialTest import LexerInitialTest
from Tests.SymbolTableInitialTest import test

# Step by step
# Lexer -> Syntax Analyzer -> Symbols Table

def main():

    # test.addSymbolsToTableTest()
    #
    # test.shouldTableFindSymbol('number2')
    #
    # LexerInitialTest().run()

    with open("program.txt", "rt") as input:
        Lexer(input.read()).readInput()


if __name__ == "__main__":
    main()