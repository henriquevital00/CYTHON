class Token:

    type: str

    def __init__(self, type: str, value):
        self.type = type
        self.value = value

    def toString(self):
        return f"<{self.type}: {self.value}>"