def SyntaxFlaw(line, char: int):
    print("[ERROR]: SyntaxFlaw\n\t- " + line + "\n\t" + " "*(char+1) + "^\nInvalid Syntax :(\n\n- process terminated -")


def IllegalChar(line, char: int, text, illchar):
    print("[ERROR]: IllegalChar, line " + str(line) + "\n\t- " + text + "\n\t" + " "*(char+3) +
          "^\nIllegal Character \"" + illchar + "\" not accepted." + "\n\n- process terminated -")