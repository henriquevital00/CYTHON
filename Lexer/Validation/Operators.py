import re

def isOperatorToken(word):

    isArithmetic = re.match("^\+|-|\/|\*$", word)

    isLogical = "^&|\|$"


    if isArithmetic:

        if word == '+':
            return (true, Token)


    return False, None
