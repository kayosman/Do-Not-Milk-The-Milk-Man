# #!/usr/bin/env python3
import os
import sys
from entitys import *


def disclaimer():  # sourcery skip: remove-redundant-if
    print("This game WILL contain"
          "very sensitive topics such as"
          "KILLING, PROFANITY, DEGENERACY, SEX etc"
          "By typing yes you are agreeing that you are aware of what you're getting into and you are agreeing to this"
          "experience")
    x = input("-> ")
    if x == "YES" or "yes" or "ye" or "y" or "ard":
        return True
    elif x == "NO" or "no" or "n" or "nah":
        return False
    return True


def preGameStart():
    disclaimer()
    if not disclaimer():
        return sys.exit(0)
    print("Start G")


def newGameStart():
    print("Character Creation\n"
          "Male or Female \n\n"
          "This will DRASTICALLY impact your game")
    inp = input("-> ")


def main():
    pass


if __name__ == '__main__':
    main()
