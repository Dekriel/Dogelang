def SyntaxFlaw(line, char: int, reason):
    print("[ERROR]: SyntaxFlaw\n\t- " + str(line) + "\n\t" + " "*(char+1) + "^\nInvalid Syntax: " + reason)


def IllegalChar(line, char: int, text, illchar):
    print("[ERROR]: IllegalChar, line " + str(line) + "\n\t- " + text + "\n\t" + " "*(char+3) +
          "^\nIllegal Character \"" + illchar + "\" not accepted." + "\n\n- process terminated -")

def IndexingProblem(line, char: int):
    print("[ERROR]: IndexingProblem\n\t- " + str(line) + "\n\t" + " "*(char+1) + "^\nIndex out of range")
