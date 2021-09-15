from Tokens import Token


class Symbol:

    name: str
    type: str
    scope: str
    instance: "Symbol"

    def __init__(self, token: Token, scope: str) -> None:
        self.name = token.value
        self.type = token.type
        self.scope = scope
        self.address = self.getSymbolAddress(self)

    def getSymbolAddress(self, symbol: "Symbol") -> str:
        """
            Get the symbol's memory address
            :param symbol: provided symbol
            :return:
        """
        return hex(id(symbol))

    def ToString(self) -> str:
        return f"[{self.scope}] <{self.type}: {self.name}> at {self.address}"
