from typing import Any

class Token:

    type: str
    value: Any

    def __init__(self, type: str, value: Any):
        self.type = type
        self.value = value

    def toString(self):
        return f"<{self.type}: {self.value}>"