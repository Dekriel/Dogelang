from dogelang_errors.errors import *

# variables
dogelangVariables = {}
ABOUT = {
    "$println":
        "$println(...)\n\tprints the text given. Use '%' around your variable name to print the value.",

    "$declare":
        "$declare ... = ...\n\tdeclares a variable with it's own value.\nList of different types you can create:\n\t- "
        "createList(): creates a array.\n\t- createDict: creates a dictionary.\n\t- createTuple(): creates an "
        "immutable list. "
}


class Compiler:
    def __init__(self, text):
        self.txt = text
        self.OPEN_SCOPE = {}
        self.printtext = ""
        self.full = ""
        for i in self.txt:
            self.full += i

    def compile_text(self):
        global dogelangVariables

        if not self.txt:
            pass

        elif self.txt[0] == "$println":
            x = ""
            should_concat = False
            for i in dogelangVariables.keys():
                for elem in self.txt:
                    if elem == f"%{i}%":
                        ind = self.txt.index(elem)
                        self.txt.remove(elem)
                        self.txt.insert(ind, dogelangVariables[elem.replace("%", "")])

            for elem in self.txt:

                if elem == '(':
                    should_concat = True
                if elem != '$println' and should_concat:
                    x += elem
            raw = x.replace("(", "")
            raw2 = raw.replace(")", "")
            if raw2 in dogelangVariables:
                x = f"(\"{dogelangVariables[raw2]}\")"

            try:

                eva_string = "print"+x
                eval(eva_string)
            except SyntaxError as err:
                SyntaxFlaw(x, err.lineno, err.args[0])

        elif self.txt[0] == "$declare":
            x = ""
            if self.txt[4] == "=":
                if self.txt[5] != " ":
                    for i in range(5, len(self.txt)):
                        x += self.txt[i]

                elif self.txt[5] == " ":
                    for i in range(6, len(self.txt)):
                        x += self.txt[i]

            if x == "createList()":
                x = "[]"

            elif x == "createDict()":
                x = "{}"

            elif x == "createTuple()":
                x = "()"

            try:
                exec(self.txt[2] + " = " + str(x))
            except SyntaxError as err:
                SyntaxFlaw(x, err.lineno, err.args[0])
            dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

        elif self.txt[0] == "$checkif":
            try:
                strip1 = [x.strip('"') for x in self.txt]
                strip2 = [x.strip('') for x in strip1]
                print("yes")
                check_thing = strip2[1]
                check_what = strip2[2]
                check_is = strip2[3]
                print(strip2)

                if check_thing in dogelangVariables:
                    check_thing = dogelangVariables[check_thing]

                if check_is in dogelangVariables:
                    check_is = dogelangVariables[check_is]

                print(check_thing)
                print(check_what)
                print(check_is)

                if check_what == "==":
                    if check_thing == check_is:
                        print(True)
                    else:
                        print(False)

                elif check_what == ">":
                    return check_thing > check_is

                elif check_what == "<":
                    return check_thing < check_is

                elif check_what == "<=":
                    return check_thing <= check_is

                elif check_what == ">=":
                    return check_thing >= check_is

                else:
                    return None
            except IndexError as err:
                SyntaxFlaw(self.full, len(self.full), "invalid syntax")
        else:
            if self.txt[0] == "///":
                pass

            else:
                SyntaxFlaw(self.txt[0], len(self.txt[0]), "invalid syntax")
