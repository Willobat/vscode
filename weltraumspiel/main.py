#weltraumbild Galaxie downscaled


import math
import time
import os

WIDTH = 600
HEIGHT = 500
SPEED = 6

class Player:
    def __init__ (self):
        self.actor = Actor("spaceship")
        self.actor.pos = (WIDTH // 2, HEIGHT // 1.1)
    def show(self):
        self.actor.draw()
    def update(self):
        if keyboard.a:
            self.actor.x -= SPEED
    
        if keyboard.d:
            self.actor.x += SPEED   

player = Player()

def draw():
    screen.clear()
    player.show()
    
def update():
    player.update()




