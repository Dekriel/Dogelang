import sys
from parser import parser


def shell():
    while True:
        try:
            t = input("dogelang > ")
            # easter eggs
            if t == "include <hello>":
                print("hello there")

            # custom builtins
            elif t == "help()":
                while True:
                    e = input(">> ")
                    print("ok" + " " + e)

            else:
                print(parser(t).get_values())
        except KeyboardInterrupt:
            print("\nended process")
            break


if __name__ == '__main__':
    globals()[sys.argv[1]]()
