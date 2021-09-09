from Symbols.SymbolsTable.SymbolsTable import SymbolsTable

class CompilerCore:

    SymbolsTable: "SymbolsTable"

    def __init__(self):
        self.SymbolsTable = SymbolsTable()

core = CompilerCore()

