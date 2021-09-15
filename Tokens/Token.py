from enum import Enum
from typing import Any

class Token:

    type: str
    value: Any

    def __init__(self, type: str, value: Any):
        self.type = type
        self.value = value