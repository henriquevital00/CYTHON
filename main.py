from Lexer.Lexer import Lexer
import re
from Tests.LexerInitialTest import LexerInitialTest
from Tests.SymbolTableInitialTest import test
from core import core
from Parser.Parser import Parser


"""
MAIN
"""

def main() -> None:
    """
    The program starts here.
    Main method will read the .cy file and throw it to the lexer

    :return: None
    """

    #  TESTE TABELA DE SÍMBOLOS
    # test.addSymbolsToTableTest()

    # TESTES LEXER
    # LexerInitialTest().run()

    with open("program.cy", "rt") as input:
        core.Lexer = Lexer(input.read())
        core.Lexer.readInput()

    Parser().parseGrammar()


if __name__ == "__main__":
    main()