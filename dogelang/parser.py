class parser:
    def __init__(self, command=None, file=None):
        self.line_num = 1
        self.line_content = []
        self.cmd = command.strip()
        self.line_parsed = []
        self.file = file

    def get_values(self):
        # parse the values appropriate for the compiler to sense
        self.line_content = [i for i in self.cmd]

        # add a <END> to mark the end of the line.
        self.line_content.append("<END>")
        c = ""
        if self.line_content[0] == " ":
            pass
        for j, char in enumerate(self.line_content):
            # list of things we want to ignore
            if char in (" ", "", ",", ".", ";", '"', "(", ")", "<END>", '=', '+', "'", "///"):
                if len(c) != 0:
                    self.line_parsed.append(c)
                c = ""

            elif char == "\n":
                break

            else:
                c += char

            # list of things we don't want to ignore
            if char in ('"', ".", "(", ")", ",", "///", '=', '+', "'"):
                self.line_parsed.append(char)
        return self.line_parsed

    def compiler_values(self):
        line_split = self.cmd.split(' ')
        if line_split[0] == '$checkif' or line_split[0] == '$fn':
            self.line_parsed = line_split
        else:
            self.line_content = [i for i in self.cmd]
            self.line_content.append("<END>")
            c = ""
            if self.line_content[0] == " ":
                pass

            for j, char in enumerate(self.line_content):
                if char in (" ", ",", ".", ";", '"', "(", ")", "<END>", '=', '+', "'", "///"):
                    if len(c) != 0:
                        self.line_parsed.append(c)
                    c = ""

                elif char == "\n":
                    break

                else:
                    c += char

                if char in ('"', ".", "(", ")", ",", '=', '+', "'", " "):
                    self.line_parsed.append(char)

        return self.line_parsed

    def get_from_file(self):
        with open(self.file, "r+") as f:
            for line in f.readlines():
                print(parser(line.strip()).get_values())

            f.close()

    @classmethod
    def get(cls, load):
        r = []
        for line in load.splitlines():
            r.extend(cls(line.strip()).get_values())
        return r
