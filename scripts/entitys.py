class Entity:
    def __init__(self, name, evil):
        self.name = name
        self.evil = evil

    def changeName(self, newName):
        self.name = newName
    
    def isEvil(self):
        return self.evil


class Player(Entity):
    def __init__(self, health):
        self.health = health
        self._health = health
        
    def die(self):
        def isAlive(self):
            if(self.health <= self._health):
                return False
        isAlive()
        if(self.isAlive() == False):
            print("You Died")   

class monsters(Entity):
    pass
        
