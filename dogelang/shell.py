import sys
from compiler import Compiler, ABOUT
from parser import parser


def shell():
    print("Dogelang 2022 ver 0.0.1\nType 'help', 'credits', or 'about' for more information")
    while True:
        try:
            t = input("dogelang > ")
            # easter eggs
            if t == "include <hello>":
                print("hello there")

            # custom builtins
            elif t == "help":
                print("Welcome to the Dogelang 0.0.1 help utility!\n\nenter the name of any builtin, keyword or topic "
                      "\nto get help on writing Dogelang programs and using Dogelang builtins. To quit this utility, "
                      "\nsimply type 'quit'.\n")
                while True:
                    e = input("dogelang_help>> ")
                    if e == "quit":
                        break

                    elif e == "quit()":
                        print("Type 'quit' to quit.")

                    if e in ABOUT.keys():
                        print(ABOUT[e])

                    else:
                        print("No documentation found for '%s'." % e)

            else:
                Compiler(parser(t).compiler_values()).compile_text()
        except KeyboardInterrupt:
            print("\nended process")
            break


if __name__ == '__main__':
    globals()[sys.argv[1]]()
