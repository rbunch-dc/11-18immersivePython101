import os
from Hero import Hero

hero_name = raw_input("WHat is your name, brave one?")
theHero = Hero(hero_name, 8)
theHero.cheer_hero()

while(1):

    message = """You have %d health and %d power.
    The goblin has %d health and %d power.
    What do you want to do?
    1. fight goblin
    2. do a little dance
    3. flee""" 
    print message % (theHero.health,theHero.power,goblin_health,goblin_power)
    # Get the user's choice
    user_input = raw_input("> ")

    if user_input == "1":
        # The hero has decided to attack!
        # subtract goblins health by hero power
        goblin_health -= theHero.power
        print "You have done %d damage to the goblin!" % hero_power
    elif user_input == "2":
        theHero.health += 10
        print """The goblin stares at you in disbelief of your stupidity. 
        His jaw drops as your wounds heal."""
        print "Your health is now %d" % theHero.health
    elif user_input == "3":
        print "Goodbye, cowardly %s" % hero_name
        # the break statement will end the loop IMMEDIATELY!!
        break
    else:
        # user entered something that we didnt offer
        print "Thou fool. Thou hast stumbledith (invalid input)"
    # Now, it's the goblin's turn
    # unless he just died from the hero attack
    if goblin_health > 0:
        hero_health -= goblin_power
        print "The goblin hits you for %d damage" % goblin_power
        if hero_health <= 0:
            print "Thou hast been slain."
    # else:
        # os.system("say Hooray. Thou hast killed the goblin!")
    if hero_health < 5:
        print "%s has gone into a rage as death appraoches. Power increased!" % hero_name
        hero_power += 5
    raw_input("Hit enter to conntinue")
    os.system("clear")