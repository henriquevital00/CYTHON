def isLiteralExpression(parser) -> tuple:
    if self.current_token.type in (
            TokenTypes.NUMBER_LITERAL,
            TokenTypes.BOOLEAN_LITERAL,
            TokenTypes.STRING_LITERAL
    ):
        literalToken = self.current_token
        self.eat(self.current_token.type)

        if literalToken.type == TokenTypes.STRING_LITERAL:
            return StringExpression(literalToken)

        elif literalToken.type == TokenTypes.BOOLEAN_LITERAL:
            return BooleanExpression(literalToken)

        else:
            return NumberExpression(literalToken)