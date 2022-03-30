# #!/usr/bin/env python3
import os
import sys
from entitys import *
from Weapons import *
import time

def main():
    pass

if __name__ == '__main__':
    player = Player("Bob", False, 100, 1, 0)
    count = 0
    while(True):
        ran = random.randrange(100)
        time.sleep(1)
        if(ran <= 50):
            dagger = Dagger()
            dagger.generateStats()
            print(f"|{dagger.name}| |Level:{dagger.weaponLevel}| |Damage:{dagger.damage}| |{dagger.value} Gold|")
            count += 1
            if(count == 30):
                sys.exit(0)
        elif(ran >= 50):
            sword = Sword()
            sword.generateStats()
            print(f"|{sword.name}| |Level:{sword.weaponLevel}| |Damage:{sword.damage}| |{sword.value} Gold|")
            count += 1
            if(count == 30):
                sys.exit(0)