from Parser.SyntaxNode.SyntaxNode import SyntaxNode


class SyntaxMatcher:

    @staticmethod
    def restoreTokenCursor(parser, oldPosition) -> None:
        """
        Restore the original cursor position

        :param oldPosition: original cursor position
        """
        parser.current_token = parser._lexer.getNextToken(oldPosition)
        parser._position = oldPosition

    @staticmethod
    def checkSyntax(syntaxValidators, parser) -> SyntaxNode or None:
        """
        Try parse some syntax node based in the passed validators.

        :param syntaxValidators: tuple with the syntax node type and its corresponding parse function
        :param parser: Parser instance

        :returns: SyntaxNode or None
        """
        oldPosition = parser._position

        for syntaxType, syntaxParse in syntaxValidators:
            expression = syntaxParse()

            if isinstance(expression, syntaxType):
                return expression

            SyntaxMatcher.restoreTokenCursor(parser, oldPosition)