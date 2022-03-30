class Entity:
    def __init__(self, name, evil):
        self.name = name
        self.evil = evil

    def changeName(self, newName):
        self.name = newName
    
    def isEvil(self):
        return self.evil


class Player(Entity):
    def __init__(self, name="Person", evil=False, health=100, level=1, exp=0):
        super().__init__(name, evil)
        self.health = health
        self._health = health
        self.level = level
        self.exp = exp
    @staticmethod
    def getLevel():
        return Player.level
    
    def setLevel(self, newLevel):
        self.level = newLevel

    def isAlive(self):
        if(self.health <= self._health - self._health):
            print("You died")
            return False
        else:
            return True
        
    def checkHealth(self):
        if(self.health > self._health):
            self.health = self._health
            print(f"{self.health} + {self._health}")
            return True
        else:
            return False
        
    def levelUp(self):
        healthMultiplier = self.health * 1.5
        levelCap = self.health / 4
        if(self.exp >= levelCap):
            self.level += 1
            self.health += healthMultiplier
            
class monsters(Entity):
    pass

