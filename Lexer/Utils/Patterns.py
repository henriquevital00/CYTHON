import re

isSeparator = lambda char : char is not None and re.match("^;|\s|\\n$", char)

isWhitespace = lambda char : char is not None and char.isspace()

isPoint = lambda char : char == "."

isArithmeticOperator = lambda char : re.match("^\+|-|\*|/$", char)

isCloseParenthesis = lambda char : char == ")"

isLetterOrNumber = lambda char : re.match("^\w$", char)

isQuote = lambda char : re.match("^\"|'$", char)
