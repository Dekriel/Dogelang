from parser import parser


class Compiler:
    def __init__(self, text):
        self.txt = text
        self.OPEN_SCOPE = 0
        self.printtext = ""

    def compile_text(self):
        print(self.txt)
        if self.txt[0] == "$println":
            x = ""
            for elem in self.txt:
                if elem != '$println' and elem != '(' and elem != '"' and elem != ')':
                    x += elem
            print(x)


Compiler(parser("$println('hello world')").compiler_values()).compile_text()
