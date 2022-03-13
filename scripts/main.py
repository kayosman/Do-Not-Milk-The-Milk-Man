# #!/usr/bin/env python3
import os
import sys
from entitys import *


def disclaimer():  # sourcery skip: remove-redundant-if
    print("This game WILL contain "
          "very sensitive topics such as "
          "KILLING, PROFANITY, DEGENERACY, SEX etc "
          "By typing yes you are agreeing that you are aware of what you're getting into and you are agreeing to this "
          "experience ")
    x = input("-> ")
    if x == "yes" or "y":
        return True
    elif x == "no":
        sys.exit(0)
    else:
        print("type (yes) or (no)")
        return disclaimer()


def preGameStart():
    print("Start Game")


def newGameStart():
    print("Character Creation\n"
          "Male or Female \n\n"
          "This will DRASTICALLY impact your game")
    inp = input("-> ")


def main():
    disclaimer()
    preGameStart()
    newGameStart()


if __name__ == '__main__':
    main()
