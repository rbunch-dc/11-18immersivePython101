# Arrow needs to be a subclass of Sprite.
# so that we can add it to a group

from pygame.sprite import Sprite

class Arrow(Sprite):
    def __init__(self,theHero):
        super(Arrow,self).__init__()
        self.x = theHero.x
        self.y = theHero.y
        self.speed = 25
    def update_me(self):
        self.x += self.speed