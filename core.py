from Symbols.SymbolsTable.SymbolsTable import SymbolsTable
from Lexer.Lexer import Lexer

class CompilerCore:
    """
    Contains the global compiler instances to be injected in other classes
    """

    SymbolsTable: "SymbolsTable" = SymbolsTable()
    Lexer: Lexer

core = CompilerCore()
