from enum import Enum

#------- ABREVIACOES REGEX---------
# \d = [0-9]
# \l = [a-z] | [A-Z] | á | à | â | ã | é | è | ê | í | ï | ó | ô | õ | ö | | ú | ç | ñ | Á | À | Â |Ã | É | È | Í | Ï | Ó | Ô | Õ | Ö | Ú| Ç | Ñ
# \w = \d | \l | \z
# \z =  [ | } | { | , | . | ^ | ~ | ? | = | + | _ | / | - | + | '*' | ] | ! | @ | \n | \t | \r

#                   TIPOS DOS TOKENS
# =======================================================
#  KEYWORD = palavra reservada
#  OPERATORS = operadores lógicos, de comparação e aritméticos
#  IDENTIFIER = identificadores de variáveis
#  DELIMITER = delimitadores de linha e escopo
#  ESCAPE_CHARACTER = caracteres de escape
#  LITERALS_TYPES = caracteres para valores literais


class TokenTypes(Enum):
    KEYWORD = 0
    OPERATOR = 1
    IDENTIFIER = 2
    DELIMITER = 3
    ESCAPE_CHARACTER = 4
    LITERALS_TYPES = 5
    SCOPE = 6
