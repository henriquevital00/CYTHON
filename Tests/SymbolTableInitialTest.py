from core import core
from Tokens.Token import Token
from Utils.Constants.Scope import ScopeConstants
from Symbols.Symbol import Symbol
from Tokens.Types.Variables.Identifier.Identifier import IdentifierToken

class SymbolTableInitalTest:

    _symbolsTable = core.SymbolsTable

    def __init__(self):
        pass

    def addSymbolsToTableTest(self):

        symbol = Symbol(Token(IdentifierToken.IDENTIFIER.name, "number1"), ScopeConstants.LOCAL)
        symbol2 = Symbol(Token(IdentifierToken.IDENTIFIER.name, "string1"), ScopeConstants.LOCAL)

        self._symbolsTable.storeSymbol(symbol)
        self._symbolsTable.storeSymbol(symbol2)

        print("Added Symbols:")
        self._symbolsTable.findAllSymbols()

        print()
        self._symbolsTable.storeSymbol(symbol)


    def shouldTableFindSymbol(self, key):

        symbol = self._symbolsTable.findSymbolByKey(key)

test = SymbolTableInitalTest()
