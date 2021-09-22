from enum import Enum

class LiteralsTokens(Enum):

    NUMBER_LITERAL = '^-?\d+(.\d+)?$'
    STRING_LITERAL = """^(".*")|('.*')$"""
    BOOLEAN_LITERAL = "^True|False$"