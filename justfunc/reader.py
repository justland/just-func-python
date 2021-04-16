import sys
from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class Tokenizer:
    src: str
    pos: int = 0
    tokens: List[Any] = field(default_factory=list)

    def tokenize(self):
        while not self.eof():
            ch = self.advance()
            if ch in "[]{}":
                self.tokens.append(ch)
            elif ch in ", \n\r\t":
                continue
            elif ch.isdigit():
                value = ch
                while self.peek().isdigit():
                    value += self.advance()
                if self.peek() == ".":
                    value += self.advance()
                    while self.peek().isdigit():
                        value += self.advance()
                self.tokens.append(value)
            elif ch.isalpha():
                value = ch
                while self.peek().isalpha():
                    value += self.advance()
                self.tokens.append(value)
            elif ch == '"':
                value = ""
                while self.peek() != '"' and not self.eof():
                    value += self.advance()
                self.advance()
                self.tokens.append(value)
            else:
                raise RuntimeError(f"Unexpected character: {ch}")
        return self.tokens

    def eof(self):
        return self.pos >= len(self.src)

    def advance(self):
        if self.eof():
            return "\0"
        self.pos += 1
        return self.src[self.pos-1]

    def peek(self, offset=0):
        if self.pos + offset >= len(self.src):
            return "\0"
        return self.src[self.pos + offset]


@dataclass
class Parser:
    tokens: List[Any]
    pos: int = 0

    def parse(self):
        token = self.advance()
        if token.strip() == ",":
            return self.parse()
        if token == "{":
            a_dict = {}
            while not self.peek() == "}" and not self.eof():
                key = self.parse()
                value = self.parse()
                a_dict.update({key: value})
            self.advance()
            return a_dict
        if token == "[":
            a_list = []
            while not self.peek() == "]" and not self.eof():
                a_list.append(self.parse())
            self.advance()
            return a_list
        return atom(token)

    def advance(self):
        if self.eof():
            return None
        self.pos += 1
        return self.tokens[self.pos - 1]

    def peek(self):
        if self.eof():
            return None
        return self.tokens[self.pos]

    def eof(self):
        return self.pos >= len(self.tokens)


@dataclass(frozen=True)
class Symbol:
    value: str


def atom(token):
    if token == "null":
        return None
    if token.isnumeric():
        return int(token)
    if "." in token and all(p.isnumeric() for p in token.split(".", 1)):
        return float(token)
    if token.startswith("'") and token.endswith("'"):
        return token[1:-1]
    return Symbol(sys.intern(token))


def read(src):
    return Parser(Tokenizer(src).tokenize()).parse()
