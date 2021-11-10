from Lexer.Lexer import Lexer
from Parser.Extensions import ArithmeticParseExtensions, LogicalParseExtensions, ComparisonParseExtensions, \
    ConditionalParseExtensions, SimpleStatementExtensions, SelectionStatementExtensions, CompoundStatementExtensions, \
    LiteralExtensions, IdentifierExtensions
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

    with open("program.cy", "rt") as input:
        core.Lexer = Lexer(input.read())
        core.Lexer.readInput()

    configureParsingExtensions()
    parser = Parser()

    syntaxTree = parser.parse()
    parser.transpile(syntaxTree)

    showUserOptions(syntaxTree)

def showUserOptions(syntaxTree):
    option = 0

    while option != 3:
        option = int(input(f"\nChoose an option:"
              f"\n1 - Show syntax tokens"
              f"\n2 - Show syntax tree"
              f"\n3 - Close cython compiler options\n"))

        if option == 1:
            core.Lexer.prettyTokensPrint()

        elif option == 2:
            print(syntaxTree)

        print()

def configureParsingExtensions():
    ArithmeticParseExtensions.addExtensions()
    LogicalParseExtensions.addExtensions()
    ComparisonParseExtensions.addExtensions()
    ConditionalParseExtensions.addExtensions()
    SimpleStatementExtensions.addExtensions()
    SelectionStatementExtensions.addExtensions()
    CompoundStatementExtensions.addExtensions()
    LiteralExtensions.addExtensions()
    IdentifierExtensions.addExtensions()

if __name__ == "__main__":
    main()