import string
import sys
import random



if __name__ == "__main__":
    print(f"Python version in number  :: {sys.winver}")
    print(f"Python version :: {sys.version}")
    print(f"Python version :: {sys.executable}")

    print(f"Help :: {help(random)}")
    print(f"Help :: {type(random)}")
    print([n for n in dir(string) if not n.startswith("_")])