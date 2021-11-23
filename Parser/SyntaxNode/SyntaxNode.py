from abc import ABC, abstractmethod

class SyntaxNode(ABC):

    @abstractmethod
    def getChildren(self) -> list:
        """
            Get the children of a specific node

            :return None
        """
        pass