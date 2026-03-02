#weltraumbild Galaxie downscaled


import math
import time
import os

WIDTH = 600
HEIGHT = 800

class Player:
    def __init__ (self):
        self.actor = Actor("spaceship")
        self.actor.pos = (WIDTH // 2, HEIGHT // 1.1)
    def show(self):
        self.actor.draw()
       
player = Player()

def draw():
    player.show()

def update():
    pass



