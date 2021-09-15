from Symbols.Symbol import Symbol
from Symbols.SymbolsTable.Exceptions.SymbolAlreadyDeclared import SymbolAlreadyDeclared
from Symbols.SymbolsTable.Exceptions.SymbolNotFound import SymbolNotFoundException

class SymbolsTable:

    _storedSymbols: dict = {}

    def __init__(self):
        pass

    def storeSymbol(self, symbol: Symbol) -> None:
        """
            Store a provided symbol in the table

            :param symbol: symbol to be stored
            :return:
        """
        try:
            if self._storedSymbols.get(symbol.name) is None:
                self._storedSymbols[symbol.name] = symbol
            else:
                raise SymbolAlreadyDeclared(symbol)

        except SymbolAlreadyDeclared as ex:
            print(ex.message)

    def findSymbolByKey(self, key: str) -> Symbol:
        """
            Find symbol according a provided key

            :param key: provided symbol key
            :return: found symbol key
        """
        try:

            if self._storedSymbols.get(key) is None:
                raise SymbolNotFoundException(key)

            symbol = self._storedSymbols[key]
            return symbol

        except SymbolNotFoundException as ex:
            print(ex.message)


    def findAllSymbols(self):
        """
            Find and print all table stored symbols

            :return:
        """
        for symbol in self._storedSymbols.values():

            print(symbol, end='  :  ')
            print(symbol.toString())
