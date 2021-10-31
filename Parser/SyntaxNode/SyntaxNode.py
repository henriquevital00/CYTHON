from abc import ABC, abstractmethod

class SyntaxNode(ABC):

    @abstractmethod
    def getChildren(self) -> list:
        pass