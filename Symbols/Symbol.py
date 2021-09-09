class Symbol:

    Name: str
    Type: str
    scope: str
    instance: "Symbol"

    def __init__(self, name, type):
        self.Name = name
        self.Type = type
        self.Address = self.getSymbolAddress(self)

    def getSymbolAddress(self, symbol: "Symbol") -> str:
        """
            Get the symbol's memory address
            :param symbol: provided symbol
            :return:
        """
        return hex(id(symbol))

    def ToString(self):
        return f"<{self.Type}: {self.Name}> at {self.Address}"
