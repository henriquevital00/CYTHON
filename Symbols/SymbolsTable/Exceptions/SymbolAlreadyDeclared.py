from Symbols import Symbol

class SymbolAlreadyDeclared(Exception):

    def __init__(self, symbol: Symbol):
        self.message = f"{symbol.type} with name {symbol.name} already declared in {symbol.scope} scope"