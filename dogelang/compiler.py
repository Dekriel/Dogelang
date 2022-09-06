import random

from dogelang_errors.errors import *
from parser import *

# variables
dogelangScopes = 0
dogelangClosed = 0
dogelangVariables = {}
dogelangBlocks = []
dogelangFunctions = {}
ABOUT = {
    "$println":
        "$println(...)\n\tprints the text given. Use '%' around your variable name to print the value.",

    "$declare":
        "$declare ... = ...\n\tdeclares a variable with it's own value.\nList of different types you can create:\n\t- "
        "createList(): creates a array.\n\t- createDict: creates a dictionary.\n\t- createTuple(): creates an "
        "immutable list. ",
}


class Compiler:
    def __init__(self, text):
        self.txt = text
        self.OPEN_SCOPE = 0
        self.printtext = ""
        self.full = ""
        for i in self.txt:
            self.full += i
        self.x = ""

    def compile_text(self):
        global dogelangVariables
        global dogelangBlocks
        global dogelangScopes

        if not self.txt:
            pass

        elif self.txt[0] == ' ':
            while True:
                if self.txt[0] == ' ':
                    self.txt.pop(0)
                else:
                    break

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
            if raw2 in dogelangVariables.keys():
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
                    dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

                elif self.txt[5] == " ":
                    for i in range(6, len(self.txt)):
                        x += self.txt[i]
                    dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

            else:
                SyntaxFlaw(self.full, 4, 'invalid syntax')

            for _ in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if self.txt[2].startswith(_):
                    SyntaxFlaw(self.full, 10, 'Invalid Syntax')

            if x == "createList()":
                x = "[]"
                dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

            elif x == "createDict()":
                x = "{}"
                dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

            elif x == "createTuple()":
                x = "()"
                dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

            elif x.startswith("$receiveint"):
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
                    if elem != '$receive' and should_concat:
                        x += elem
                raw = x.replace("(", "")
                raw2 = raw.replace(")", "")
                raw2 = raw2.strip('"')

                if raw2 in dogelangVariables:
                    x = f"(\"{dogelangVariables[raw2]}\")"

                ans = input(raw2)
                x = int(ans)
                dogelangVariables[self.txt[2]] = x

            elif x.startswith("$receive"):
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
                    if elem != '$receive' and should_concat:
                        x += elem
                raw = x.replace("(", "")
                raw2 = raw.replace(")", "")
                raw2 = raw2.strip('"')

                if raw2 in dogelangVariables:
                    x = f"(\"{dogelangVariables[raw2]}\")"

                ans = input(raw2)
                x = "\""+ans+"\""
                dogelangVariables[self.txt[2]] = x.strip('\"').replace("'", "")

            elif x.startswith("$random"):
                r = parser(x).compiler_values()
                x = random.randint(int(r[2]), int(r[5]))
                dogelangVariables[self.txt[2]] = x

        elif self.txt[0] == "$checkif":
            try:
                strip1 = [x.strip('"') for x in self.txt]
                strip2 = [x.strip('') for x in strip1]
                strip2.pop(0)

                check_HasScope = False
                check_thing = ""
                check_what = ""
                check_is = ""
                e = 0

                for i in strip2:
                    e += 1
                    if i in [">=", "<=", "==", ">", "<"]:
                        check_is = i

                    elif i in [">=", "<=", "=="] and check_thing == "":
                        SyntaxFlaw(self.full, e, "invalid syntax")

                    elif i not in ["<=", ">=", "=="] and check_is != "":
                        if i == "{":
                            while True:
                                a = input("... ")
                                if a == "}":
                                    check_HasScope = True
                                    break
                                else:
                                    dogelangBlocks.append(a)
                        else:
                            check_what += i

                    elif i not in ["<=", ">=", "=="]:
                        check_thing += i

                if check_thing in dogelangVariables:
                    check_thing = dogelangVariables[check_thing]

                if check_what in dogelangVariables:
                    check_what = dogelangVariables[check_is]

                if check_is == "==":
                    if check_what == check_thing:
                        if check_HasScope:
                            for i in dogelangBlocks:
                                Compiler(parser(i[1:]).compiler_values()).compile_text()

                            dogelangBlocks = []

                elif check_is == ">":
                    if check_what > check_thing:
                        if check_HasScope:
                            for i in dogelangBlocks:
                                Compiler(parser(i[1:]).compiler_values()).compile_text()

                            dogelangBlocks = []

                elif check_is == "<":
                    if check_what < check_thing:
                        if check_HasScope:
                            for i in dogelangBlocks:
                                Compiler(parser(i[1:]).compiler_values()).compile_text()

                            dogelangBlocks = []

                elif check_is == "<=":
                    if check_what <= check_thing:
                        if check_HasScope:
                            for i in dogelangBlocks:
                                Compiler(parser(i[1:]).compiler_values()).compile_text()

                            dogelangBlocks = []

                elif check_is == ">=":
                    if check_what >= check_thing:
                        if check_HasScope:
                            for i in dogelangBlocks:
                                Compiler(parser(i[1:]).compiler_values()).compile_text()

                            dogelangBlocks = []
                else:
                    return None

            except IndexError:
                SyntaxFlaw(self.full, len(self.full), "invalid syntax")

        elif self.txt[0] == "$receive":
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
                if elem != '$receive' and should_concat:
                    x += elem
            raw = x.replace("(", "")
            raw2 = raw.replace(")", "")
            raw2 = raw2.strip('"')

            if raw2 in dogelangVariables:
                x = f"(\"{dogelangVariables[raw2]}\")"

            ans = input(raw2)

        elif self.txt[0] == "$while":
            if self.txt[2] == "TRUE":
                for i in self.txt:
                    if i == "{":
                        while True:
                            a = input("... ")
                            if a == "}":
                                break
                            else:
                                dogelangBlocks.append(a)
            while True:
                for i in dogelangBlocks:
                    if i == "BREAK":
                        dogelangBlocks = []
                        break
                    else:
                        Compiler(parser(i[1:]).compiler_values()).compile_text()
        else:
            if self.txt[0] == "///":
                pass

            else:
                print("Not identified :(")
