from entitys import *
import math
import random

class Weapons:
    def __init__(self, name, damage, weaponLevel):
        self.damage = damage
        self.name = name
        self.weaponLevel = weaponLevel
        self.weaponReq = math.floor(self.weaponLevel / 8)
        self.value = self.value = (self.weaponLevel + self.damage) * self.weaponLevel 
       
    def checkLevel(self):
        if(Player.self >= self.weaponReq):
            return True
        elif(Player.self <= self.weaponReq):
            print("You're not a high Player.self")
            return False
        
    def changeName(self, newName):
        self.name = newName
        
    def getName(self):
        return self.name
    
    def setName(self):
        if (self.weaponLevel < 5):
            self.changeName(f"Horrible {self.name}")        
        elif (self.weaponLevel <= 10):
            self.changeName(f"Poop {self.name}")
        elif (self.weaponLevel <= 15):
            self.changeName(f"Shit {self.name}")
        elif (self.weaponLevel <= 20):
            self.changeName(f"Ai {self.name}")
        elif (self.weaponLevel <= 25):
            self.changeName(f"Ok {self.name}")
        elif (self.weaponLevel <= 30):
            self.changeName(f"Really ok {self.name}")
        elif (self.weaponLevel <= 35):
            self.changeName(f"Good {self.name}")
        elif (self.weaponLevel <= 40):
            self.changeName(f"Gooder {self.name}")
        elif (self.weaponLevel <= 45):
            self.changeName(f"Goodest {self.name}")
        elif (self.weaponLevel <= 50):
            self.changeName(f"Great {self.name}")
        elif (self.weaponLevel <= 55):
            self.changeName(f"Greater {self.name}")
        elif (self.weaponLevel <= 60):
            self.changeName(f"Greatest {self.name}")
        elif (self.weaponLevel <= 65):
            self.changeName(f"Best {self.name}")
        elif (self.weaponLevel <= 70):
            self.changeName(f"Bester {self.name}")
        elif (self.weaponLevel <= 75):
            self.changeName(f"Bestest {self.name}")
        elif (self.weaponLevel <= 80):
            self.changeName(f"God teir {self.name}")
        elif (self.weaponLevel <= 85):
            self.changeName(f"Insane {self.name}")
        elif (self.weaponLevel <= 90):
            self.changeName(f"Holy shit {self.name}")
        elif (self.weaponLevel <= 95):
            self.changeName(f"Bruh {self.name}")
        elif (self.weaponLevel <= 1, 100):
            self.changeName(f"Bruh^2 {self.name}")
        elif (self.weaponLevel <= 150):
            self.changeName(f"OP {self.name}")
        elif (self.weaponLevel <= 200):
            self.changeName(f"OP REWORKED {self.name}")
        else:
            self.changeName(f"N-WORD PASS")
     
            
class Sword(Weapons, Player):
    def __init__(self, name="Sword", damage=2, weaponLevel=1):
        super().__init__(name, damage, weaponLevel)
        self.rarity = random.randrange(self.weaponLevel)
        self.value = self.value = (self.weaponLevel + self.damage) * self.weaponLevel
        
    def getRarity(self):
        return self.rarity
    
    def getWeaponLevel(self):
        return self.level
    
    def generateStats(self):
        damageMultiplier = random.randrange(1,3)
        if(math.floor(random.randrange(1, 100)) <= 25):
            if(random.randrange(1, 100) < 5):
                self.weaponReq / 1.5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 1.2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 12):
                self.weaponReq / 1.5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 1.9)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 15):
                self.weaponReq / 1.5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 25):
                self.weaponReq / 1.5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 2.4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            else:
                self.weaponReq / 1.5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 3)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()    
        elif(math.ceil(random.randrange(1, 100)) >= 50):
            if(random.randrange(1, 100) < 5):
                self.weaponReq / 2
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 12):
                self.weaponReq / 2
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 2.9)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 15):
                self.weaponReq / 2
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 3)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 25):
                self.weaponReq / 2
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 3.4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            else:
                self.weaponReq / 2
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
        elif(math.ceil(random.randrange(1, 100)) >= 75):
            if(random.randrange(1, 100) < 5):
                self.weaponReq / 3
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 3.2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 12):
                self.weaponReq / 3
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 4.9)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 15):
                self.weaponReq / 3
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 5)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 25):
                self.weaponReq / 3
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 6.4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            else:
                self.weaponReq / 3
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 7)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
        elif(math.ceil(random.randrange(1, 100)) <= 85):
            if(random.randrange(1, 100) < 5):
                self.weaponReq / 4
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 4.2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 12):
                self.weaponReq / 4
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 5.9)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 15):
                self.weaponReq / 4
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 6)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 25):
                self.weaponReq / 4
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 7.4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            else:
                self.weaponReq / 4
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 8)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
        elif(math.ceil(random.randrange(1, 100)) >= 3):
            if(random.randrange(1, 100) < 5):
                self.weaponReq / 5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 7.2)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 12):
                self.weaponReq / 5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 8)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 15):
                self.weaponReq / 5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 8.4)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            elif(random.randrange(1, 100) > 25):
                self.weaponReq / 5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 9)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
            else:
                self.weaponReq / 5
                self.weaponLevel = math.ceil(random.randrange(random.randrange(1, 100)) * 10)
                self.damage = math.ceil(self.weaponLevel * damageMultiplier)
                self.setName()
     

# class Dagger(Weapons):
#     def __init__(self, name, damage, weaponLevel):
#         super().__init__(name, damage, weaponLevel)
#         self.rarity = random.randrange(self.weaponLevel)
        
#     def getRarity(self):
#         return self.rarity
    
#     def generateStats(self):
#         damageMultiplier = random.randrange(3)
#         if(math.floor(random.randrange(1, 100)) <= 25):
#             if(random.randrange(1, 100) < 5):
#                 self.weaponReq / 1.5
#                 self.weaponLevel = math.floor(random.randrange(random.randrange(1, 100)) * 1.2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(random.randrange(1, 100) > 12):
#                 self.weaponReq / 1.5
#                 self.weaponLevel = math.floor(random.randrange(random.randrange(1, 100)) * 1.9)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(random.randrange(1, 100) > 15):
#                 self.weaponReq / 1.5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 25):
#                 self.weaponReq / 1.5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 2.4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             else:
#                 self.weaponReq / 1.5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 3)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()    
#         elif(math.floor(random.randrange(1, 100)) >= 50):
#             if(Player.self < 5):
#                 self.weaponReq / 2
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 12):
#                 self.weaponReq / 2
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 2.9)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 15):
#                 self.weaponReq / 2
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 3)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 25):
#                 self.weaponReq / 2
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 3.4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             else:
#                 self.weaponReq / 2
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#         elif(math.floor(random.randrange(1, 100)) >= 75):
#             if(Player.self < 5):
#                 self.weaponReq / 3
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 3.2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 12):
#                 self.weaponReq / 3
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 4.9)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 15):
#                 self.weaponReq / 3
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 5)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 25):
#                 self.weaponReq / 3
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 6.4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             else:
#                 self.weaponReq / 3
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 7)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#         elif(math.floor(random.randrange(1, 100)) <= 85):
#             if(Player.self < 5):
#                 self.weaponReq / 4
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 4.2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 12):
#                 self.weaponReq / 4
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 5.9)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 15):
#                 self.weaponReq / 4
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 6)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 25):
#                 self.weaponReq / 4
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 7.4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             else:
#                 self.weaponReq / 4
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 8)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#         elif(math.floor(random.randrange(1, 100)) >= 95):
#             if(Player.self < 5):
#                 self.weaponReq / 5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 7.2)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 12):
#                 self.weaponReq / 5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 8)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 15):
#                 self.weaponReq / 5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 8.4)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             elif(Player.self > 25):
#                 self.weaponReq / 5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 9)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
#             else:
#                 self.weaponReq / 5
#                 self.weaponLevel = math.floor(random.randrange(Player.self) * 10)
#                 self.damage = math.floor(self.weaponLevel * damageMultiplier)
#                 self.setName()
     