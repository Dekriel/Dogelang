class parser:
    def __init__(self, command):
        self.line_num = 1
        self.line_content = []
        self.cmd = command
        self.line_parsed = []

    def get_values(self):
        self.line_content = [i for i in self.cmd]
        c = ""
        if self.line_content[0] == " ":
            pass

        for j in range(len(self.line_content)):
            if self.line_content[j] == " ":
                self.line_parsed.append(c)
                c = ""
            elif self.line_content[j] == ";":
                self.line_parsed.append(c)

            elif self.line_content[j] == "\"":
                self.line_parsed.append("\"")

            else:
                c += self.line_content[j]

        print(self.line_parsed)


parser("hello \"there\";").get_values()
