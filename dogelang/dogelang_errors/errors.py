def SyntaxFlaw(line, char: int):
    print("[ERROR]: SyntaxFlaw\n\t- " + line + "\n\t" + " "*(char+1) + "^\nInvalid Syntax :(\n\n- process terminated -")


def IllegalChar(line, char: int, illchar):
    print("[ERROR]: IllegalChar\n\t- " + line + "\n\t" + " "*(char+1) +
          "^\nIllegal Character \"" + illchar + "\" not accepted." + "\n\n- process terminated -")
