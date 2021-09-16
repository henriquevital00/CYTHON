from Tests.SymbolTableInitialTest import test

# Step by step
# Lexer -> Syntax Analyzer -> Symbols Table

def main():

    test.addSymbolsToTableTest()

    test.shouldTableFindSymbol('number2')

if __name__ == "__main__":
    main()