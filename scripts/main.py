# #!/usr/bin/env python3
import os
import sys
from entitys import *
from Weapons import *
import time

def main():
    pass

if __name__ == '__main__':
    x = 0
    monster = Monster()
    while(x < 10):
        monster.generateMonsterName()
        print(f"{monster.name} {monster.level}")
        x += 1
    thicc = Monster()
    while(x < 20):
        thicc.level = 45
        thicc.generateMonsterName()
        print(f"{thicc.name} {thicc.level}")
        x += 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # while(True):
    #     ran = random.randrange(100)
    #     time.sleep(1)
    #     if(ran <= 25):
    #         dagger = Dagger()
    #         dagger.generateStats()
    #         print(f"|{dagger.name}| |Level:{dagger.weaponLevel}| |Damage:{dagger.damage}| |{dagger.value} Gold|")
    #         count += 1
    #         if(count == 30):
    #             sys.exit(0)
    #     elif(ran <= 50):
    #         sword = Sword()
    #         sword.generateStats()
    #         print(f"|{sword.name}| |Level:{sword.weaponLevel}| |Damage:{sword.damage}| |{sword.value} Gold|")
    #         count += 1
    #         if(count == 30):
    #             sys.exit(0)
    #     elif(ran <= 75):
    #         spear = Spear()
    #         spear.generateStats()
    #         print(f"|{spear.name}| |Level:{spear.weaponLevel}| |Damage:{spear.damage}| |{spear.value} Gold|")
    #         count += 1
    #         if(count == 30):
    #             sys.exit(0)
    #     else:
    #         hammer = Hammer()
    #         hammer.generateStats()
    #         print(f"|{hammer.name}| |Level:{hammer.weaponLevel}| |Damage:{hammer.damage}| |{hammer.value} Gold|")
    #         count += 1
    #         if(count == 30):
    #             sys.exit(0)