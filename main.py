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
    Parser().parse()


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