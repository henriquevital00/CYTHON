from typing import Any

class Token:
    """
        Represents the compiler tokens:
        chars that when joined form a token
    """

    type: str
    """Token type"""

    value: Any
    """Token value"""

    def __init__(self, type: str, value) -> None:
        self.type = type
        self.value = value

    def toString(self) -> str:
        """
            Convert token to string representation

            :return: token string
        """
        return f"< {self.type}: {self.value} >"