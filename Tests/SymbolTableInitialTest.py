from core import core
from Symbols.Symbol import Symbol
from Tokens.Definitions.Variables.VarTypes.VarTypes import VariableTypesTokens
from Tokens.Definitions.Scope.Scope import ScopeTokens

class SymbolTableInitalTest:

    _symbolsTable = core.SymbolsTable

    def __init__(self):
        pass

    def addSymbolsToTableTest(self):

        symbol = Symbol("number1", VariableTypesTokens.NUMBER, ScopeTokens.LOCAL)
        symbol2 = Symbol("string1", VariableTypesTokens.STRING, ScopeTokens.LOCAL)

        self._symbolsTable.StoreSymbol(symbol)
        self._symbolsTable.StoreSymbol(symbol2)

        print("Added Symbols:")
        self._symbolsTable.FindAllSymbols()

        print()
        self._symbolsTable.StoreSymbol(symbol)


    def shouldTableFindSymbol(self, key):

        symbol = self._symbolsTable.FindSymbolByKey(key)

test = SymbolTableInitalTest()
