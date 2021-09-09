from enum import Enum
from Tokens.Token import Token

class Symbol:

    Name: str
    Type: Token
    Scope: Token
    instance: "Symbol"

    def __init__(self, name, type: Enum, scope: Enum):
        self.Name = name
        self.Type = type.value
        self.Scope = scope.value
        self.Address = self.getSymbolAddress(self)

    def getSymbolAddress(self, symbol: "Symbol") -> str:
        """
            Get the symbol's memory address
            :param symbol: provided symbol
            :return:
        """
        return hex(id(symbol))

    def ToString(self):
        return f"[{self.Scope.Name}] <{self.Type.Name}: {self.Name}> at {self.Address}"
