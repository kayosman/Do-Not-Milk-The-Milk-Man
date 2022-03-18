# #!/usr/bin/env python3
import os
import sys
from entitys import *

def main():
    pass

if __name__ == '__main__':
    monster = monsters("Maria", True)
    print(f"moster name: {monster.name} and {monster.evil}")
    monster.changeName("Trent")
    print(f"moster name: {monster.name} and {monster.evil}")