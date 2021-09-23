from Tokens import Token

class Symbol:
    """
        Stored entities during program execution, like variables and functions
    """

    name: str
    """Symbol name"""

    type: str
    """Symbol type"""

    scope: str
    """The scope in which the symbol was declared"""

    instance: "Symbol"
    """The symbol instance"""

    def __init__(self, token: Token, scope: str) -> None:
        self.name = token.value
        self.type = token.type
        self.scope = scope
        self.address = self.getSymbolAddress(self)

    def getSymbolAddress(self, symbol: "Symbol") -> str:
        """
            Get the symbol's memory address

            :param symbol: provided symbol

            :return: symbol address
        """
        return hex(id(symbol))

    def toString(self) -> str:
        """
            Convert symbol to string representation

            :return: symbol string
        """
        return f"[{self.scope}] <{self.type}: {self.name}> at {self.address}"
