from Symbols.Symbol import Symbol
from Symbols.SymbolsTable.Exceptions.SymbolAlreadyDeclared import SymbolAlreadyDeclared
from Symbols.SymbolsTable.Exceptions.SymbolNotFound import SymbolNotFoundException

class SymbolsTable:
    """Store the identified symbols during the program execution"""

    _storedSymbols: dict = {}

    def __init__(self) -> None:
        pass

    def storeSymbol(self, symbol: Symbol) -> None:
        """
            Store a provided symbol in the table

            :param symbol: symbol to be stored
            :return: None

            :raises: SymbolAlreadyDeclared
                exception raised if a symbol has already been declared
        """
        if self._storedSymbols.get(symbol.name) is None:
            self._storedSymbols[symbol.name] = symbol
        else:
            raise Exception(f"{symbol.type} with name '{symbol.name}' already declared")

    def findSymbolByKey(self, key: str) -> Symbol:
        """
            Find symbol according a provided key

            :param key: provided symbol key
            :return: found symbol key

        """
        if self._storedSymbols.get(key) is None:
            raise Exception(f"Not found symbol with provided key: <{key}>")

        symbol = self._storedSymbols[key]
        return symbol

    def findAllSymbols(self) -> None:
        """
            Find and print all table stored symbols

            :return: None
        """
        for symbol in self._storedSymbols.values():

            print(symbol, end='  :  ')
            print(symbol.toString())

    def updateSymbol(self, symbolName, symbolValue):
        symbol = self.findSymbolByKey(symbolName)
        symbol.value = symbolValue