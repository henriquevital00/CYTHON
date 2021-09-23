from enum import Enum

class DelimitersTokens(Enum):
    """Enum class for delimiters tokens"""

    OPEN_SCOPE = '^{$'
    """type: OPEN_SCOPE
    
    regex: ^{$"""

    END_SCOPE = '^}$'
    """type: END_SCOPE
    
    regex: ^}$"""

    END_COMMAND = '^;$'
    """type: END_COMMAND    
    
    regex: ^;$"""

    L_PAREN = '^\($'
    """type: L_PAREN   
     
    regex: ^\($"""

    R_PAREN = '^\)$'
    """type: R_PAREN
    
    regex: ^\)$"""