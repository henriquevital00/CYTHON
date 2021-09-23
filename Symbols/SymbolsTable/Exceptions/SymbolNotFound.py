class SymbolNotFoundException(Exception):
    """Class responsible for raise exception if a symbol was not found"""

    def __init__(self, key: str, message: str = "Not found symbol with provided key: ") -> None:
        """
        :param key: key of symbols table
        :param message: message of error
        :return: None
        """
        self.message = f"{message} <{key}>"