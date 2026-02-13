__all__ = ["Parser"]

import re
from ..dsl import MolangExpr
from .ast import Ternary, Binary, Unary, Number, Variable, Assign, Call, Node
from .tokenizer import tokenize


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if expected and token != expected:
            raise SyntaxError(f"Expected {expected}, got {token}")
        self.pos += 1
        return token

    def parse(self) -> Node:
        return self.parse_assignment()

    def parse_assignment(self) -> Node:
        expr = self.parse_ternary()
        if self.peek() == "=":
            self.consume("=")
            right = self.parse_ternary()
            if self.peek() == ";":
                self.consume(";")
            return Assign(expr, right)
        return expr

    def parse_ternary(self) -> Node:
        expr = self.parse_or()
        if self.peek() == "?":
            self.consume("?")
            true = self.parse_ternary()
            self.consume(":")
            false = self.parse_ternary()
            return Ternary(expr, true, false)
        return expr

    def parse_or(self) -> Node:
        expr = self.parse_and()
        while self.peek() == "||":
            op = self.consume()
            right = self.parse_and()
            expr = Binary(expr, op, right)
        return expr

    def parse_and(self) -> Node:
        expr = self.parse_equality()
        while self.peek() == "&&":
            op = self.consume()
            right = self.parse_equality()
            expr = Binary(expr, op, right)
        return expr

    def parse_equality(self) -> Node:
        expr = self.parse_comparison()
        while self.peek() in ("==", "!="):
            op = self.consume()
            right = self.parse_comparison()
            expr = Binary(expr, op, right)
        return expr

    def parse_comparison(self) -> Node:
        expr = self.parse_term()
        while self.peek() in (">", "<", ">=", "<="):
            op = self.consume()
            right = self.parse_term()
            expr = Binary(expr, op, right)
        return expr

    def parse_term(self) -> Node:
        expr = self.parse_factor()
        while self.peek() in ("+", "-"):
            op = self.consume()
            right = self.parse_factor()
            expr = Binary(expr, op, right)
        return expr

    def parse_factor(self) -> Node:
        expr = self.parse_unary()
        while self.peek() in ("*", "/"):
            op = self.consume()
            right = self.parse_unary()
            expr = Binary(expr, op, right)
        return expr

    def parse_unary(self) -> Node:
        if self.peek() in ("!", "-"):
            op = self.consume()
            return Unary(op, self.parse_unary())
        return self.parse_primary()

    def parse_primary(self) -> Node:
        token = self.peek()

        if token is None:
            raise SyntaxError("Unexpected end")

        if token == "(":
            self.consume("(")
            expr = self.parse_ternary()
            self.consume(")")
            return expr

        if re.match(r"\d", token):
            self.consume()
            return Number(token)

        self.consume()
        var = Variable(token)

        # Check for function call
        if self.peek() == "(":
            self.consume("(")
            args = []
            if self.peek() != ")":
                args.append(self.parse_ternary())
                while self.peek() == ",":
                    self.consume(",")
                    args.append(self.parse_ternary())
            self.consume(")")
            return Call(var, args)

        return var


def parse_expression(expr: str | MolangExpr) -> Node:
    tokens = tokenize(expr)
    return Parser(tokens).parse()
