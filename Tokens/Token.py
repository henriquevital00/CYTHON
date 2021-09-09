from enum import Enum

class Token:

    Name: str
    Type: str

    def __init__(self, name, type: Enum):
        self.Name = name
        self.Type = type.value