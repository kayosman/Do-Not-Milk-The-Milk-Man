import random

class Entity:
    def __init__(self, name, evil):
        self.name = name
        self.evil = evil

    def isEvil(self):
        return self.evil


class Player(Entity):
    def __init__(self, name="Person", evil=False, health=100, level=1, exp=0):
        super().__init__(name, evil)
        self.health = health
        self._health = health
        self.level = level
        self.exp = exp
    
    def getLevel(self):
        return self.level
    
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
            
class Monster(Entity):
    def __init__(self, name= "Monster", evil=True, level=1):
        super().__init__(name, evil)
        self.level = level
        
    def generateMonsterName(self):
        __lowLevelNames = ['Vexpest', 
                         'Flamemutant',
                         'The Calm Man',
                         'Hellpest',
                         'Poor Black Man',
                         'Scary Cow',
                         'Wild Crip Member',
                         'Flamecrackle',
                          'Hauntbrute',
                          'Gasvine',
                          'Big Penis',
                          'Black Man',
                          'Gallhand',
                         'azorflayer',
                          'Bull',
                          'Spectralscream',
                          'Putridpest',
                          'Wisphag',
                          'Wild Blood' 'Member',
                          'Wet Cow',
                          'Cow',
                          'Wondering Homeless Person',
                          'Poisoncrackle',
                          'The Ashy Gorilla',
                          'Gloompaw',
                          'Wondering Bald Man',
                          'Curseflayer',
                          'Milk Mans Sister',
                          'The Calm Brute',
                          'Fetidpest',
                          'Phantomfoot',
                          'Milking Cow']
        
        __midLevelNames = ["The Agile Dweller",
                           "The Anguished Monstrosity",
                           "The Bitter Presence",
                           "The Black-Eyed Venom Elephant",
                           "The Bloodthirsty Night Fiend",
                           "The Bright Ghost Snake",
                           "The Canine Vermin",
                           "The Cobalt Venom Viper",
                           "The Cold-Blooded Doom Elephant",
                           "The Crazed Rot Beast",
                           "The Dead Malformation",
                           "The Diabolical Army Tiger",
                           "The Electric Freak",
                           "The Enraged Entity",
                           "The Fiery World Gargoyle",
                           "The Grim Blob",
                           "The Grisly Mocking Serpent",
                           "The Haunting Being",
                           "The Hollow",
                           "Bradley",
                           "The Agitated Wraith",
                           "The Awful Mumbler",
                           "The Bewitched Entity",
                           "The Blissful Deformity",
                           "The Blissful Deformity",
                           "The Bloodthirsty Razor Behemoth",
                           "The Bold Statue",
                           "The Bold Statue",
                           "The Bronze Howler",
                           "The Cold-Blooded Mountain Frog",
                           "The Cold-Blooded Mountain Frog",
                           "The Colossal Savage, The Delirious Pest",
                           "The Diabolical Preying Beast",
                           "The Diabolical Preying Beast",
                           "The Dreary Figure",
                           "The Ebon Cave Leopard", 
                           "The Ebon Mountain Jackal", 
                           "The Ebon Mountain Jackal",
                           "The Electric Cinder Cat",
                           "The Feathered Raptor Frog",
                           "The Feathered Rot Boar",
                           "The Filthy Ooze",
                           "The Filthy Plant",
                           "The Filthy Plant",
                           "The Hidden Dire Jackal",
                           "The Living Revenant",
                           "The Masked Nightmare Owl",
                           "The Primeval Demon Hound",
                           "The Ravaging World Owl"]
        
        if(self.level <= 10):
            x = random.choice(__lowLevelNames)
            self.name = x
        elif(self.level <= 50):
            x = random.choice(__midLevelNames)
            self.name = x
    
    
