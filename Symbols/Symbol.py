from typing import Any

class Symbol:
    """
        Stored entities during program execution, like variables and functions
    """

    name: str
    """Symbol name"""

    type: str
    """Symbol type"""

    value: Any

    def __init__(self, type, name, value) -> None:
        self.type = type
        self.name = name
        self.value = value

    def toString(self) -> str:
        """
            Convert symbol to string representation

            :return: symbol string
        """
        return f"[<{self.type}: {self.name}>"
