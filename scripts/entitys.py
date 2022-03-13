def isEvil(entity):
    return bool(entity)


class Entity:
    def __init__(self, name, evil):
        self.name = name
        self.evil = evil

    def changeName(self, newName):
        self.name = newName


class Player(Entity):
    pass
    # def __init__(self, name, evil):
    #     super().__init__(name, evil)
    #     self.name = name

