from enum import Enum


class ComparisonOperatorsTokens(Enum):

    GREATER = '^>$'
    LESS = '^<$'
    EQUALS = '^==$'
    GREATER_EQUALS = '^>=$'
    LESS_EQUALS = '^<=$'