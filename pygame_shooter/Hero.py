import pygame

class Hero(object):
    # classes always contain 2 parts:
    # 1. the __init__ = runs only once
    # 2. the methods = run whenever you call them
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_up = False
    def shouldMove(self,direction):
        if direction == "right":
            self.should_move_right = True
        if direction == "left":
            self.should_move_left = True
        if(direction == "down"):
            self.should_move_down = True
        if(direction == "up"):
            self.should_move_up = True
        