# 1. Include pygame
# we needed pip to get this for us because Python doesnt ship with it
import pygame
from Hero import Hero
from BadGuy import BadGuy
from Arrow import Arrow
from Button import Start_Button

# we want to have pygame "groups"
from pygame.sprite import Group,groupcollide

# 2. Initialize Pygame.
# Why do we need to do this? Because they told us to.
pygame.init()

# 3. Make a screen with a size. The size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption('Robin Hood')

theHero = Hero()
bad_guy = BadGuy()
# make a bad_guys group
bad_guys = Group()
# add the bad_guy to the bad_guys group
bad_guys.add(bad_guy)
# make a start button
start_button = Start_Button(pygame_screen)

# make a group for our arrows to live in
# a group is a pygame thing. Its like a list,
# but with cool stuff too
arrows = Group()

# ========VARIABLES FOR OUR GAME==========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
tick = 0
# heroLoc = {
#     'x': 100,
#     'y': 100
# }
direction = 1
# =========MAIN GAME LOOP==========
game_on = True
game_start = False
# the loop will run as long as our bool is true
while game_on:
    # we are in the game loop from here on out!
    # 5. Listen for events and quit if the user clicks the x
    # =======EVENT CHECKER=========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # THE USER CLICKED THE RED DOT!
                # These aren't the droids were looking for. quit.
                game_on = False
        elif event.type == pygame.KEYDOWN:
            # the user pressed a key!!!
            print event.key
            if event.key == 275:
                # the user pressed the right arrow!!! Move our dude right
                # heroLoc['x'] += 10
                # theHero.x += 10
                theHero.shouldMove("right")
            elif event.key == 276:
                # the user pressed left arrow!
                # theHero.x -= 10
                theHero.shouldMove("left")
            if event.key == 273:
                # the user pressed the up arrow!
                theHero.shouldMove("up")
            elif event.key == 274:
                theHero.shouldMove("down")
            elif event.key == 32:
                # user pressed space bar... FIRE!!!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)
                # print arrows
        elif event.type == pygame.KEYUP:
            # the user RELEASED a key
            if event.key == 275:
                theHero.shouldMove("right",False)
            elif event.key == 276:
                theHero.shouldMove("left",False)
            if event.key == 273:
                theHero.shouldMove("up",False)
            elif event.key == 274:
                theHero.shouldMove("down",False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			# print mouse_x,mouse_y;
			if start_button.rect.collidepoint(mouse_x, mouse_y):
				game_start = True
				bg_music = pygame.mixer.Sound('faf.wav')
				bg_music.play()


    # ==========DRAW STUFF===========
    # we use blit to draw on the screen. blit = block image transfer
    # blit is a method, that takes 2 arg:
    # 1. What to draw
    # 2. Where to draw it
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[tick,tick])
    if game_start == True:
        theHero.draw_me(512,480)
        for bad_guy in bad_guys:
            bad_guy.update_me(theHero)
            pygame_screen.blit(monster_image,[bad_guy.x,bad_guy.y])

        for arrow in arrows:
            arrow.update_me()
            pygame_screen.blit(arrow_image,[arrow.x,arrow.y])
        pygame_screen.blit(hero_image,[theHero.x,theHero.y])

        arrow_hit = groupcollide(arrows,bad_guys,True,True)
        # print arrow_hit
        if arrow_hit:
            bad_guys.add(BadGuy())

    if game_start == False:
        start_button.setup_message()
        start_button.draw_button()
    
    pygame.display.flip()