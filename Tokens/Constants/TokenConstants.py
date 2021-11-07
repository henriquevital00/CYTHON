class TokenTypes:

    # region DELIMITERS
    OPEN_SCOPE = 'OPEN_SCOPE'
    END_SCOPE = 'END_SCOPE'
    END_COMMAND = 'END_COMMAND'
    L_PAREN = 'L_PAREN'
    R_PAREN = 'R_PAREN'
    #endregion

    # region ESCAPE CHARS
    WHITESPACE = 'WHITESPACE'
    NEW_LINE = 'NEW_LINE'
    TAB = 'TAB'
    # endregion

    # region LITERALS
    NUMBER_LITERAL = 'NUMBER_LITERAL'
    STRING_LITERAL = 'STRING_LITERAL'
    BOOLEAN_LITERAL = 'BOOLEAN_LITERAL'
    # endregion

    # region OPERATORS
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    DIVISION = 'DIVISION'
    MULTIPLY = 'MULTIPLY'

    VAR_ASSIGN = 'ASSIGN_OPERATOR'

    GREATER = 'GREATER'
    LESS = 'LESS'
    EQUALS = 'EQUALS'
    GREATER_EQUALS = 'GREATER_EQUALS'
    LESS_EQUALS = 'LESS_EQUALS'
    DIFFERENT = 'DIFFERENT'

    AND = 'AND'
    OR = 'OR'
    # endregion

    # region STATEMENTS
    IF = 'IF'
    ELSE = 'ELSE'
    ELIF = 'ELIF'

    WHILE = 'WHILE'
    FOR = 'FOR'

    PRINT = 'PRINT'
    INPUT = 'INPUT'
    # endregion

    # region VARIABLES
    IDENTIFIER = 'IDENTIFIER'
    TYPE_NUMBER = 'TYPE_NUMBER'
    TYPE_STRING = 'TYPE_STRING'
    TYPE_BOOLEAN = 'TYPE_BOOLEAN'
    # endregion

    EOF = 'EOF'

