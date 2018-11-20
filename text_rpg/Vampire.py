from random import randint
# import random

class Vampire(object):
    def __init__(self):
        # randomPower = random.randint(2,5)
        randomPower = randint(4,7)
        self.name = "Vampire"
        self.health = 15
        self.power = randomPower
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage
    def is_alive(self):
        return self.health > 0
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds."