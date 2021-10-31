class SyntaxMatcher:

    @staticmethod
    def restoreTokenCursor(parser, oldPosition):
        parser.current_token = parser._lexer.getNextToken(oldPosition)
        parser._position = oldPosition

    @staticmethod
    def checkSyntax(syntaxValidators, parser):

        for syntaxType, syntaxParse in syntaxValidators:
            oldPosition = parser._position
            expression = syntaxParse()

            if isinstance(expression, syntaxType):
                return expression

            SyntaxMatcher.restoreTokenCursor(parser, oldPosition)






