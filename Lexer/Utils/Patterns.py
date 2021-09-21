import re

isSeparator = lambda char : re.match("^;|\\s|\\n$", char)

isWhitespace = lambda char : re.match("^ $", char)

isPoint = lambda char : char == "."

isEquals = lambda char : char == "="

isUnderscore = lambda char : char == "_"

isArithmeticOperator = lambda char : re.match("^\+|-|\*|/$", char)

isLogicalOperator = lambda char : re.match("^&|\|", char)

isComparisonOperator = lambda char : re.match("^<|>|=$")

isOperator = lambda char : isLogicalOperator(char) or isComparisonOperator(char) or isArithmeticOperator(char)

isBiggerOrLessOperator = lambda char : re.match("^<|>$", char)

isCloseParenthesis = lambda char : char == ")"

isLetterOrNumber = lambda char : re.match("^\w$", char)

isQuote = lambda char : re.match("^\"|'$", char)

