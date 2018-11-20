import os
# from [NAMEOFFILE] import [CLASS]
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from random import randint

hero_name = raw_input("WHat is your name, brave one?")
# There is only one Frodo
theHero = Hero(hero_name, 8)
theHero.cheer_hero()

while(theHero.is_alive()):
    # There are many, many monsters.
    # get random Monster
    randMonster = randint(1,2)
    if randMonster == 1:
        monster = Goblin()
    else:
        monster = Vampire()

    print "You have encounterd the terrifying %s" % monster.name
    while(theHero.is_alive() and monster.is_alive()):

        message = """You have %d health and %d power.
        The %s has %d health and %d power.
        What do you want to do?
        1. fight %s
        2. do a little dance
        3. flee""" 
        print message % (theHero.health,theHero.power,monster.name, monster.health, monster.power, monster.name)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack!
            # subtract monsters health by hero power
            monster.take_damage(theHero.power)
            print "You have done %d damage to the monster!" % theHero.power
        elif user_input == "2":
            theHero.health += 10
            print """The monster stares at you in disbelief of your stupidity. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d" % theHero.health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            # the break statement will end the loop IMMEDIATELY!!
            break
        else:
            # user entered something that we didnt offer
            print "Thou fool. Thou hast stumbledith (invalid input)"
        # Now, it's the monster's turn
        # unless he just died from the hero attack
        if monster.is_alive():
            theHero.take_damage(monster.power)
            print "The monster hits you for %d damage" % monster.power
            if theHero.is_alive() == False:
                print "Thou hast been slain."
        else:
            # os.system("say Hooray. Thou hast killed the monster!")
            print "Thou hast killed the monster!"
        if theHero.health < 5:
            print "%s has gone into a rage as death appraoches. Power increased!" % hero_name
            theHero.power += 5
        raw_input("Hit enter to continue")
        os.system("clear")