from Symbols.SymbolsTable.SymbolsTable import SymbolsTable

class CompilerGlobals:

    SymbolsTable: "SymbolsTable"

    def __init__(self):
        self.SymbolsTable = SymbolsTable()

core = CompilerGlobals()

