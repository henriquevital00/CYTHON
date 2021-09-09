from Symbols import Symbol

class SymbolAlreadyDeclared(Exception):

    def __init__(self, symbol: Symbol):
        self.message = f"{symbol.Type.Name} with name {symbol.Name} already declared in {symbol.Scope} scope"