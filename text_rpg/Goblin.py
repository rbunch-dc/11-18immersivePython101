from random import randint
# import random

class Goblin(object):
    def __init__(self):
        # randomPower = random.randint(2,5)
        randomPower = randint(2,5)
        self.name = "Goblin"
        self.health = 6
        self.power = randomPower
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage
    def is_alive(self):
        return self.health > 0