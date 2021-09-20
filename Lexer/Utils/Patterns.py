import re

isSeparator = lambda char : re.match("^;|\s|\\n$", char)

isWhitespace = lambda char : char.isspace()

isPoint = lambda char : char == "."

isArithmeticOperator = lambda char : re.match("^\+|-|\*|/$", char)

isCloseParenthesis = lambda char : char == ")"

isLetterOrNumber = lambda char : re.match("^\w$", char)

isQuote = lambda char : re.match("^\"|'$", char)
