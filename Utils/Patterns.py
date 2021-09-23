import re

"""
Methods responsible for validate chars literals
"""

isSeparator = lambda char : re.match("^;|\\s|\\n$", char)

isWhitespace = lambda char : re.match("^ $", char)

isPoint = lambda char : char == "."

isEquals = lambda char : char == "="

isUnderscore = lambda char : char == "_"

isLetter = lambda char : re.match("^[a-z]|[A-Z]$", char)

isArithmeticOperator = lambda char : re.match("^\+|-|\*|/$", char)

isLogicalOperator = lambda char : re.match("^&|\|", char)

isComparisonStarter = lambda char : re.match("^<|>|=|!$", char)

isOperator = lambda char : isLogicalOperator(char) \
                           or isComparisonStarter(char)\
                           or isArithmeticOperator(char)

isBiggerOrLessOperator = lambda char : re.match("^<|>$", char)

isCloseParenthesis = lambda char : char == ")"

isOpener = lambda char : re.match("^{|\($", char)

isCloser = lambda char : re.match("^\)|}$", char)

isLetterOrNumber = lambda char : re.match("^\w$", char)

isQuote = lambda char : re.match("^\"|'$", char)

isMinus = lambda char : char == "-"

isFloat = lambda char : re.match("^-?\d+\.\d+$", char)
