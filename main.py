from Lexer.Lexer import Lexer
from Parser.Extensions import ArithmeticParseExtensions, LogicalParseExtensions, ComparisonParseExtensions, \
    ConditionalParseExtensions, SimpleStatementExtensions, SelectionStatementExtensions, CompoundStatementExtensions, \
    LiteralsExtensions
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

    with open("program.cy", "rt") as input:
        core.Lexer = Lexer(input.read())
        core.Lexer.readInput()

    configureParsingExtensions()

    Parser().parse()


def configureParsingExtensions():
    ArithmeticParseExtensions.addExtensions()
    LogicalParseExtensions.addExtensions()
    ComparisonParseExtensions.addExtensions()
    ConditionalParseExtensions.addExtensions()
    SimpleStatementExtensions.addExtensions()
    SelectionStatementExtensions.addExtensions()
    CompoundStatementExtensions.addExtensions()
    LiteralsExtensions.addExtensions()

if __name__ == "__main__":
    main()