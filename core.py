from Symbols.SymbolsTable.SymbolsTable import SymbolsTable

class CompilerCore:
    """
    Contains the global compiler instances to be injected in other classes
    """

    SymbolsTable: "SymbolsTable"

    def __init__(self) -> None:
        self.SymbolsTable = SymbolsTable()

core = CompilerCore()

