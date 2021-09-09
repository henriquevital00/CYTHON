from Symbols import Symbol

class SymbolNotFoundException(Exception):

    def __init__(self, key: str, message: str = "Not found symbol with provided key: "):
        self.message = f"{message} <{key}>"

class SymbolAlreadyDeclared(Exception):

    def __init__(self, symbol: Symbol):
        self.message = f"{symbol.Type} with name {symbol.Name} already declared in {symbol.Scope} scope"