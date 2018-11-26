from random import randint
# this is a subclass of Character. So go get Character
from Character import Character
# import random

# class Vampire(object):
class Vampire(Character):
    def __init__(self):
        # call parent/super init method
        super(Vampire, self).__init__('Vampire',15,4)
        # randomPower = random.randint(2,5)
        # randomPower = randint(4,7)
        # self.name = "Vampire"
        # self.health = 15
        # self.power = randomPower
    # def take_damage(self,ammount_of_damage, game):
    #     self.health -= ammount_of_damage
    #     if self.is_alive():
    #         game.updateTotal(10)
    # def is_alive(self):
    #     return self.health > 0
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds."

class Bandit(object):
    def __init__(self):
        # randomPower = random.randint(2,5)
        randomPower = randint(4,7)
        self.name = "Bandit"
        self.health = 15
        self.power = randomPower
        self.importance = 2
    def take_damage(self,ammount_of_damage, game):
        self.health -= ammount_of_damage
        if self.is_alive():
            game.updateTotal(self.importance)
    def is_alive(self):
        return self.health > 0

class Hero(object):
    def __init__(self):
        self.name = "Vampire"
        self.health = 15
        self.power = 20

class Game(object):
    def __init__(self):
        self.total = 0
    def updateTotal(self,importance):
        if(importance > 5):
            self.total += 5
        else:
            self.total += 3


# vampire = Vampire()
# hero = Hero()
# game = Game()

# # hero strikes the vampre
# vampire.take_damage(hero.power,game)
# bandit.take_damage(hero.power,game)