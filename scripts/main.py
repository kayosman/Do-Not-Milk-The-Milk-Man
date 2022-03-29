# #!/usr/bin/env python3
import os
import sys
from entitys import *
from Weapons import *

def main():
    pass

if __name__ == '__main__':
    player = Player("Bob", True, 100, 1, 0)
    print(player.level)
    player.exp = 100000
    player.levelUp()
    print(player.level)
    sword = Sword("Sword", 1, 1)
    sword.generateStats()
    print(sword)