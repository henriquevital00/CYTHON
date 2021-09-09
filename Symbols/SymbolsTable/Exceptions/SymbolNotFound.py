class SymbolNotFoundException(Exception):

    def __init__(self, key: str, message: str = "Not found symbol with provided key: "):
        self.message = f"{message} <{key}>"