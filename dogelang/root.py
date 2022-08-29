# dogelang token class
from dogelang_errors.errors import *
from parser import parser


NUM = "0123456789."


class token:
    def __init__(self, _type, val):
        """
        a token contains the type and (optionally) a value. For example:
                            1   +   2
        the 1 is an INT, and the value is 1. Same goes for 2. However, the + doesn't have a value, and the type of it is
        a PLUS.
        """
        self.type = _type
        self.val = val

    def __repr__(self):
        """
        prints out the representation of the token.
        """
        if self.val:
            return f'TYPE: %s: VALUE: %s' % (self.type, self.val)
        else:
            return self.type


# Lexer
class lexer:
    def __init__(self, text):

        self.keywords = [
            ("$declare", "VAR_ASSIGN_KEYWORD"),
            ("$fn", "FUNCTION"),
            ("$if", "CHECK_KEYWORD"),
            ("$elseif", "CHECK_ELSE_IF_KEYWORD"),
            ("$else", "CHECK_ELSE_KEYWORD"),
            ("$break", "BREAK_LOOP"),
            ("$for", "FOR_LOOP"),
            ("$return", "RETURN_VALUE"),
            ("$receive", "RECEIVE_INPUT"),
            ("$class", "CLASS")
        ]

        self.text = text
        self.currchar = None
        self.position = -1  # we have a += 1 statement which starts it off at 0. Indexing starts at 0
        self.line_content = []
        self.line_parsed = []

    def get_values(self):
        self.line_content = [i for i in self.text]
        self.line_content.append("<END>")
        c = ""
        if self.line_content[0] == " ":
            pass
        for j, char in enumerate(self.line_content):
            if char in ("", ",", ";", '"', "(", ")", "<END>", '=', '+', '///'):
                if len(c) != 0:
                    self.line_parsed.append(c)
                c = ""

            elif char == "\n":
                break

            elif char == " ":
                pass

            else:
                c += char

            if char in ('"', "(", ")", ",", '=', '+', '///'):
                self.line_parsed.append(char)

        return self.line_parsed

    def next(self):
        self.position += 1

    def tokenize(self):
        e = lexer(self.text).get_values()
        x = ""
        for i in e:
            x += i

        print(eval(x))


lexer("").tokenize()
