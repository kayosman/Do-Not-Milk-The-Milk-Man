from entitys import *
import math
import random

class Weapons:
    def __init__(self, name, damage, weaponLevel):
        self.damage = damage
        self.name = name
        self.weaponLevel = weaponLevel
        self.weaponReq = math.floor(self.weaponLevel / 8)
        
    def checkLevel(self):
        if(Player.level >= self.weaponReq):
            return True
        elif(Player.level <= self.weaponReq):
            print("You're not a high enough level")
            return False
    
    def changeName(self, newName):
        self.name = newName
        
    def getName(self):
        return self.name
    
    def setName(self):
        if (self.weaponLevel < 5):
            self.changeName(f"Horrible, {self.name}")        
        elif (self.weaponLevel >= 10):
            self.changeName(f"Poop, {self.name}")
        elif (self.weaponLevel >= 15):
            self.changeName(f"Shit, {self.name}")
        elif (self.weaponLevel >= 20):
            self.changeName(f"Ai, {self.name}")
        elif (self.weaponLevel >= 25):
            self.changeName(f"Ok, {self.name}")
        elif (self.weaponLevel >= 30):
            self.changeName(f"Really ok, {self.name}")
        elif (self.weaponLevel >= 35):
            self.changeName(f"Good, {self.name}")
        elif (self.weaponLevel >= 40):
            self.changeName(f"Gooder, {self.name}")
        elif (self.weaponLevel >= 45):
            self.changeName(f"Goodest, {self.name}")
        elif (self.weaponLevel >= 50):
            self.changeName(f"Great, {self.name}")
        elif (self.weaponLevel >= 55):
            self.changeName(f"Greater, {self.name}")
        elif (self.weaponLevel >= 60):
            self.changeName(f"Greatest, {self.name}")
        elif (self.weaponLevel >= 65):
            self.changeName(f"Best, {self.name}")
        elif (self.weaponLevel >= 70):
            self.changeName(f"Bester, {self.name}")
        elif (self.weaponLevel >= 75):
            self.changeName(f"Bestest, {self.name}")
        elif (self.weaponLevel >= 80):
            self.changeName(f"God teir, {self.name}")
        elif (self.weaponLevel >= 85):
            self.changeName(f"Insane, {self.name}")
        elif (self.weaponLevel >= 90):
            self.changeName(f"Holy shit, {self.name}")
        elif (self.weaponLevel >= 95):
            self.changeName(f"Bruh, {self.name}")
        elif (self.weaponLevel >= 100):
            self.changeName(f"Bruh^2, {self.name}")
        elif (self.weaponLevel >= 105):
            self.changeName(f"Pov you play to much, {self.name}")
        elif (self.weaponLevel >= 110):
            self.changeName(f"Pov stop playing, {self.name}")
        else:
            self.changeName(f"Bruh Bruh Bruh^2")
     
            
class Sword(Weapons):
    def __init__(self, name, damage, weaponLevel):
        super().__init__(name, damage, weaponLevel)
        self.rarity = random.randrange(self.weaponLevel)
    def getRarity(self):
        return self.rarity
    
    def generateStats(self):
        damageMultiplier = random.randrange(3)
        if(math.floor(random.randrange(100)) <= 25):
            if(Player.level < 5):
                self.weaponReq / 1.5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 1.2)
                self.setName()
            elif(Player.level > 12):
                self.weaponReq / 1.5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 1.9)
                self.setName()
            elif(Player.level > 15):
                self.weaponReq / 1.5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 2)
                self.setName()
            elif(Player.level > 25):
                self.weaponReq / 1.5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 2.4)
                self.setName()
            else:
                self.weaponReq / 1.5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 3)
                self.setName()    
        elif(math.floor(random.randrange(100)) >= 50):
            if(Player.level < 5):
                self.weaponReq / 2
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 2)
                self.setName()
            elif(Player.level > 12):
                self.weaponReq / 2
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 2.9)
                self.setName()
            elif(Player.level > 15):
                self.weaponReq / 2
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 3)
                self.setName()
            elif(Player.level > 25):
                self.weaponReq / 2
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 3.4)
                self.setName()
            else:
                self.weaponReq / 2
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 4)
                self.setName()
        elif(math.floor(random.randrange(100)) >= 75):
            if(Player.level < 5):
                self.weaponReq / 3
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 3.2)
                self.setName()
            elif(Player.level > 12):
                self.weaponReq / 3
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 4.9)
                self.setName()
            elif(Player.level > 15):
                self.weaponReq / 3
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 5)
                self.setName()
            elif(Player.level > 25):
                self.weaponReq / 3
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 6.4)
                self.setName()
            else:
                self.weaponReq / 3
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 7)
                self.setName()
        elif(math.floor(random.randrange(100)) <= 85):
            if(Player.level < 5):
                self.weaponReq / 4
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 4.2)
                self.setName()
            elif(Player.level > 12):
                self.weaponReq / 4
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 5.9)
                self.setName()
            elif(Player.level > 15):
                self.weaponReq / 4
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 6)
                self.setName()
            elif(Player.level > 25):
                self.weaponReq / 4
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 7.4)
                self.setName()
            else:
                self.weaponReq / 4
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 8)
                self.setName()
        elif(math.floor(random.randrange(100)) >= 95):
            if(Player.level < 5):
                self.weaponReq / 5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 7.2)
                self.setName()
            elif(Player.level > 12):
                self.weaponReq / 5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 8)
                self.setName()
            elif(Player.level > 15):
                self.weaponReq / 5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 8.4)
                self.setName()
            elif(Player.level > 25):
                self.weaponReq / 5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 9)
                self.setName()
            else:
                self.weaponReq / 5
                self.damage = math.floor(self.weaponLevel * damageMultiplier)
                self.weaponLevel = math.floor(random.randrange(Player.level) * 10)
                self.setName()
     
     