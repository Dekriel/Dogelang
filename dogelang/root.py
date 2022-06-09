# dogelang token class

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
        self.keywords = ["set", "fn", "checkif"]

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
        self.rules = [
            ("COMMENT", r"//"),
            ("STRING", "\""),
            ("COMMA", ","),
            ("LPAREN", "("),
            ("RPAREN", ")"),
            ("LBRACKET", "["),
            ("RBRACKET", "]"),
            ("LCURL", "{"),
            ("RCURL", "}"),
            ("ASSIGN", "="),
            ("PLUS", "+"),
            ("MINUS", "-"),
            ("DIVIDE", "/"),
            ("OPERATOR", "<=|>=|<|>|=="),
            ("MULTIPLY", "*"),
            ("WHITESPACE", "\t| "),
            ("NEWLINE", "\n"),
            ("SEMICOLON", ";"),
            ("COLON", ":")
        ]

        self.keywords = [
            ("$declare", "VAR_ASSIGN_KEYWORD"),
            ("$fn", "FUNCTION"),
            ("$if", "CHECK_KEYWORD"),
            ("$elseif", "CHECK_ELSE_IF_KEYWORD"),
            ("$else", "CHECK_ELSE_KEYWORD"),
            ("$break", "BREAK_LOOP"),
            ("$for", "FOR_LOOP"),
            ("$return", "RETURN_VALUE"),
            ("$receive", "RECEIVE_INPUT")
        ]

        self.text = text
        self.currchar = None
        self.position = -1  # we have a += 1 statement which starts it off at 0. Indexing starts at 0

    def next(self):
        self.position += 1
