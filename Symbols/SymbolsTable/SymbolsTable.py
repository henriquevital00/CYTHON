from Symbols.Symbol import Symbol
from Symbols.SymbolsTable.Exceptions.SymbolNotFound import SymbolNotFoundException

class SymbolsTable:

    _storedSymbols: dict = {}

    def __init__(self):
        pass

    def StoreSymbol(self, symbol: Symbol) -> None:
        """
            Store a provided symbol in the table

            :param symbol: symbol to be stored
            :return:
        """
        self._storedSymbols[symbol.Name] = symbol


    def FindSymbolByKey(self, key: str) -> Symbol:
        """
            Find key according a provided key

            :param key: provided symbol key
            :return: found symbol key
        """
        try:

            if key not in self._storedSymbols.keys():
                raise SymbolNotFoundException(key)

            symbol = self._storedSymbols[key]
            return symbol

        except SymbolNotFoundException as ex:
            print(ex.message)


    def FindAllSymbols(self):
        """
            Find and print all table stored symbols

            :return:
        """
        for key in self._storedSymbols.keys():

            symbol = self._storedSymbols[key]

            print(symbol, end='  :  ')
            print(symbol.ToString())
