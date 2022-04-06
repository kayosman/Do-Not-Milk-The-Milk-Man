import dialoge
import random

class Entity:
    def __init__(self, name, health, evil):

        self.name = name
        self.evil = evil
        self.health = health
        self._health = health

    def isEvil(self):
        return self.evil
    
    def randomNumber(self, value):
        randNum = random.randint(0, value)
        return randNum


class Player(Entity):
    def __init__(self, level=1, exp=0):
        super().__init__(name="Player", health=100, evil=False)
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
            randomName = random.choice(__lowLevelNames)
            self.name = randomName
        elif(self.level <= 50):
            randomName = random.choice(__midLevelNames)
            self.name = randomName
        
        
class Human(Entity):
    def __init__(self, 
                 firstName="Human", 
                 lastName="Person",
                 health=100,
                 evil=False,
                 gender="male",
                 fear=0,
                 happyness=0, 
                 sexyness=0, 
                 kindness=0, 
                 anger=0, 
                 rebellious=0, 
                 slutyness=0, 
                 love=0, 
                 faith=0):

        super().__init__(health, evil)
        
        self.firstName    = firstName
        self.lastName     = lastName
        self.gender       = gender
        self.fear         = fear
        self.happyness    = happyness
        self.sexyness     = sexyness
        self.kindness     = kindness
        self.anger        = anger
        self.rebellious   = rebellious
        self.slutyness    = slutyness
        self.love         = love
        self.faith        = faith
        
    def generatePersonality(self):
        self.fear       = self.randomNumber(100)
        self.happyness  = self.randomNumber(100)
        self.sexyness   = self.randomNumber(100)
        self.kindness   = self.randomNumber(100)
        self.anger      = self.randomNumber(100)
        self.rebellious = self.randomNumber(100)
        self.slutyness  = self.randomNumber(100)
        self.love       = self.randomNumber(100)
        self.faith      = self.randomNumber(100)
        
        if( self.faith      >= 90):
            self.slutyness  -= 80
            self.rebellious -= 80
            self.kindness   += 40
            self.fear       += 20
            if(  self.slutyness   <=  0):
                 self.slutyness   ==  0
            elif(self.slutyness   > 100):
                self.slutyness    = 100
            if( self.rebellious  <=   0):
                self.rebellious  ==   0
            elif(self.rebellious  > 100):
                self.slutyness    = 100
            if( self.fear        <=   0):
                self.fear         =   0
            elif(self.fear        > 100):
                self.fear         = 100
            if( self.happyness   <=   0):
                self.happyness    =   0
            elif(self.happyness   > 100):
                self.happyness    = 100
            if( self.sexyness    <=   0):
                self.sexyness     =   0
            elif(self.sexyness    > 100):
                self.sexyness     = 100
            if( self.kindness    <=   0):
                self.kindness     =   0
            elif(self.kindness    > 100):
                self.kindness    == 100
            if( self.anger       <=   0):
                self.anger        =   0
            elif(self.anger       > 100):
                self.anger        = 100
            if( self.love        <=   0):
                self.love         =   0
            elif(self.love        > 100):
                self.love         = 100
            if( self.faith       <=   0):
                self.faith        =   0
            elif(self.faith       > 100):
                self.faith        = 100
        if(self.rebellious       >=  75):
            self.faith           +=  20
        
        self.anger = abs(self.happyness - self.anger)
    
    def generateName(self):
        maleNames = ["Kyro ",
                     "Anselm ",
                     "Carlisle ",
                     "Lucius ",
                     "Hallam ",
                     "John-Paul ",
                     "Braylen ",
                     "Faron ",
                     "Drogo ",
                     'Jo ',
                     'Clyde ',
                     'Arnold ',
                     'Tracey ',
                     'Fortune ',
                     'Haze ',
                     'Axel ',
                     "Charles ",
                     "Danny ",
                     "Ry ",
                     "Gordy ",
                     "Pearce ",
                     "Den ",
                     "Ozzy ",
                     'Roly ',
                     'Floyd ',
                     'Easton ',
                     'Frederick ',
                     'Kendrick ',
                     'Erik ',
                     'Delmar ',
                     "Davis ",
                     "Cecil ",
                     "Kennard ",
                     "Torin ",
                     "Daley ",
                     "Brennan ",
                     "Royce ",
                     'Sheridan ',
                     'Beau ',
                     'Jaxton ',
                     'Roderick ',
                     'Casimir ',
                     'Royal ',
                     'Noah ',
                     "Haydn ",
                     "Randell ",
                     "Byron ",
                     "Loren ",
                     "Satchel ",
                     "Lester ",
                     "Jere ",
                     'Eliott ',
                     'Hedley ',
                     'Kelsey ',
                     'Cyan ',
                     'Darrel ',
                     'Johnie ',
                     'Jayceon ',
                     "Olly ",
                     "Rusty ",
                     "Rayner ",
                     "Donovan ",
                     "Merrill ",
                     "Rolph ",
                     "Kasey ",
                     'Grant ',
                     'Keaton ',
                     'Gideon ',
                     'Kenelm ',
                     'Ritchie ',
                     'Elias ',
                     'Phil ',
                     "Reg ",
                     "Elvin ",
                     "Lucius ",
                     "Deven ",
                     "Rollo ",
                     "Merritt ",
                     "Corbin ",
                     'Korbin ',
                     'Spencer ',
                     'Johnathon ',
                     'Roy ',
                     'Denny ',
                     'Charles ',
                     'Brenton ',
                     "Kennith ",
                     "Raeburn ",
                     "Mickey ",
                     "Trenton ",
                     "Trent ",
                     "Brad ",
                     "Bradley ",
                     'Brady ',
                     'Connor ',
                     'Conor ',
                     'Konor ',
                     'Levy ',
                     'Levi ',
                     'Will ',
                     "William ",
                     "Kobe ",
                     "Colby ",
                     "Gavin ",
                     "Yorick ",
                     "Cyrus ",
                     "Jerry ",
                     'Cecil ',
                     'Nat ',
                     'Guy ',
                     'Jessie ',
                     'Harper ',
                     'Wilford ',
                     'Craig ',
                     "Merv ",
                     "Kenyon ",
                     "Louie ",
                     "Leon ",
                     "Farley ",
                     "Aubrey ",
                     "Stuart ",
                     'Mort ',
                     'Morty ',
                     'Finley ',
                     'Donald ',
                     'Joe ',
                     'Barack ',
                     'Kit ',
                     "Alphonso ",
                     "Kory ",
                     "Cory ",
                     "Conrad ",
                     "Red ",
                     "Fraser ",
                     "Chadwick ",
                     'Fulton ',
                     'Scottie ',
                     'Darryl ',
                     'Hendrix ',
                     'Delmar ',
                     'Finlay ',
                     'Curt ',
                     "Eldred ",
                     "Nolan ",
                     "Watson ",
                     "Sammie ",
                     "Tommy ",
                     "Kevan ",
                     "Kevin ",
                     'Jaydon ',
                     'Deven ',
                     'Devon ',
                     'Aydan ',
                     'Jay ',
                     'Silas ',
                     'Kamden ',
                     "Dexter ",
                     "Greyson ",
                     "Jeremiah ",
                     "Chace ",
                     "Chase ",
                     "Wilburn ",
                     'Dallas ',
                     'Tanner ',
                     'Jake ',
                     'Gabriel ',
                     'Gary ',
                     'Deryck ',
                     'Derrick ',
                     "Philip ",
                     "Ry ",
                     "Philipe ",
                     "John ",
                     "Lincoln ",
                     "Deemer ",
                     "Freddy ",
                     'Anderson ',
                     'Randal ',
                     'Linden ',
                     'Chip ',
                     'Lane ',
                     'Johnnie ',
                     'Kelsey ',
                     "Brandon ",
                     "Ed ",
                     "Graham ",
                     "Irvin ",
                     "Landen ",
                     "Maximilian ",
                     "Abe ",
                     'Josh ']

        femaleNames = ["Aaliyah ",
                     "Lexi ",
                     "Ruby ",
                     "Orinda ",
                     "Jodene ",
                     "Enola ",
                     "Adria ",
                     "Xavia ",
                     "Nita ",
                     'Irma ',
                     'Andrina ',
                     'Lesleigh ',
                     'Lori',
                     'Fortune ',
                     'Jayde ',
                     'Morgan ',
                     "Allycia ",
                     "Maddison ",
                     "Ry ",
                     "Linda ",
                     "Audie ",
                     "Ember ",
                     "Amber ",
                     'Mikayla ',
                     'Tillie ',
                     'Suzan ',
                     'Isabella ',
                     'Nola ',
                     'Bonnie ',
                     'Dorine ',
                     "Kendal ",
                     "Natasha ",
                     "Carry ",
                     "Charlene ",
                     "Trix ",
                     "Shyla ",
                     "Justina ",
                     'Marlene ',
                     'Marjorie ',
                     'Abbi ',
                     'Shae ',
                     'Netta ',
                     'Destinee ',
                     'Patience ',
                     "Alexia ",
                     "Alexa ",
                     "Alexis ",
                     "Victoria ",
                     "Eleanor ",
                     "Leanne ",
                     "Daniella ",
                     'Suzan ',
                     'Terra ',
                     'Kelsey ',
                     'Kinsey ',
                     'Karissa ',
                     'Josephina ',
                     'Maeghan ',
                     "Olly ",
                     "Brittania ",
                     "Lottie ",
                     "Tristin ",
                     "Sheila ",
                     "Hepsie ",
                     "Greta ",
                     'Camille ',
                     'Corie ',
                     'Sheree',
                     'Sommer ',
                     'Beatrix ',
                     'Christine ',
                     'Kaya ',
                     "Summer ",
                     "Winter ",
                     "Fall ",
                     "Spring ",
                     "Rollo ",
                     "Tamsin ",
                     "Averie ",
                     'Chastity ',
                     'Briana ',
                     'Gena ',
                     'Marion ',
                     'Celandine ',
                     'Genevieve ',
                     'Essie ',
                     "Maya ",
                     "Breanna ",
                     "Eula ",
                     "Nyla ",
                     "Sarina ",
                     "Kelly ",
                     "Annis ",
                     'Jessamyn ',
                     'Sally ',
                     'Brandi ',
                     'Kelly ',
                     'Nyree ',
                     'Caroline ',
                     'Deena ',
                     "Margaret ",
                     "Ravenna ",
                     "Bella ",
                     "Gavin ",
                     "Yorick ",
                     "Patsy",
                     "Arianna ",
                     'Patsy ',
                     'Samantha',
                     'Sunshine ',
                     'Jessie ',
                     'Parnel ',
                     'Wilford ',
                     'Craig ',
                     "Merv ",
                     "Aaliyah ",
                     "Daniella ",
                     "Madelyn ",
                     "Flora ",
                     "Aubrey ",
                     "Alexandrina ",
                     'Jamey ',
                     'Tabitha ',
                     'Lita ',
                     'Kassy ',
                     'Juliana ',
                     'Haylee ',
                     'Sharona ',
                     "Jae ",
                     "Jaylin ",
                     "Serrena ",
                     "Ciera ",
                     "Jade ",
                     "Gena ",
                     "Jemma ",
                     'Hadley ',
                     'Dulcie ',
                     'Ariyah ',
                     'Cearra ',
                     'Delores ',
                     'Kelsie ',
                     'Lorayne ',
                     "Clare ",
                     "Clara ",
                     "Racheal ",
                     "Sammie ",
                     "Breanna ",
                     "Sam ",
                     "Avery ",
                     'Sam ',
                     'Merla ',
                     'Stacey ',
                     'Chevonne ',
                     'Arleen ',
                     'Janine ',
                     'Bindy ',
                     "Kirsten ",
                     "Lee ",
                     "Clemence ",
                     "Gwenevere ",
                     "Gretta ",
                     "Sharalyn ",
                     'Audrea ',
                     'Azura ',
                     'Simone ',
                     'Victoria ',
                     'Gabby ',
                     'Amelia ',
                     'Regena ',
                     "Philip ",
                     "Hadyn ",
                     "Brenda ",
                     "Dollie ",
                     "Ryana ",
                     "Page ",
                     "Sierra ",
                     'Francine ',
                     'Tanzi ',
                     'Chanel ',
                     'Romaine ',
                     'Zavia ',
                     'Chanté ',
                     'Hilary ',
                     "Starla ",
                     "Chrissy ",
                     "Kiarra ",
                     "Kimberley ",
                     "Silvia ",
                     "Gwen ",
                     "Alysa ",
                     'Jessie ']

        if(self.gender == "male"):
            self.firstName = random.choice(maleNames)
        elif(self.gender == "female"):
            self.firstName = random.choice(femaleNames)
        else:
            raise ValueError("INVALID GENDER")
        