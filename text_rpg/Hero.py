class Hero(object):
    # what does every class have?
    def __init__(self,name,power = 5):
        self.name = name
        self.health = 10
        self.power = power
        self.xp = 0
    def cheer_hero(self):
        print "Welcome, brave %s" % (self.name)
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage
    def is_alive(self):
        # if("elixer_of_life" in self.potions):
        #     return True
        # else:
        return self.health > 0
    def getPower(self):
        if hero.weapon == "Axe"
            return 6 + self.power
        elif hero.hasVisitedWizard:
            return 1000