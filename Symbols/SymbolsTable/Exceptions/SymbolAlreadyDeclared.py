from Symbols import Symbol

class SymbolAlreadyDeclared(Exception):
    """Class responsible for  raise exception if the symbol was already declared"""

    def __init__(self, symbol: Symbol) -> None:
        """
        Constructor
        :param symbol: symbol
        :return: None
        """
        self.message = f"{symbol.type} with name {symbol.name} already declared"