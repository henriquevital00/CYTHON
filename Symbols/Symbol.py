class Symbol:

    Name: str
    Type: str
    scope: str
    instance: "Symbol"

    def __init__(self, name, type, scope):
        self.Name = name
        self.Type = type
        self.Scope = scope
        self.Address = self.getSymbolAddress(self)

    def getSymbolAddress(self, symbol: "Symbol") -> str:
        """
            Get the symbol's memory address
            :param symbol: provided symbol
            :return:
        """
        return hex(id(symbol))

    def ToString(self):
        return f"[{self.Scope}] <{self.Type}: {self.Name}> at {self.Address}"
