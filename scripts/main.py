# #!/usr/bin/env python3
import os
import sys
from entitys import *
from Weapons import *

def main():
    pass

if __name__ == '__main__':
    player = Player("Bob", False, 100, 1, 0)
    sword = Sword()
    sword.generateStats()
    print(f"|{sword.name}| |Level:{sword.weaponLevel}| |Damage:{sword.damage}| |{sword.value} Gold|")