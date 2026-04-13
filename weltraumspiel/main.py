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
    def draw(self):
        self.actor.draw()
    def update(self):
        if keyboard.a:
            self.actor.x -= SPEED
    
        if keyboard.d:
            self.actor.x += SPEED   
        keep_in_bounds(self.actor)

game_state = "start" # possible states: start/game_over/pause/playing

player = Player()

def start_screen():
    screen.draw.text(
            "WELCOME TO THE\nSPACE SHOOTER!\nPRESS ENTER TO START", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red"
        )

def keep_in_bounds(sprite):
    if sprite.left < 0:
        sprite.left =0
    if sprite.right > WIDTH:
        sprite.right = WIDTH
    if sprite.top < 0:
        sprite.top = 0
    if sprite.bottom > HEIGHT:
        sprite.bottom = HEIGHT

def draw():
    screen.clear()
    if game_state == "start":
        start_screen()
    if game_state == "playing":
        player.draw()

def update():
    player.update()

def on_key_down(key):
    global game_state
    if game_state == "start" and key == keys.RETURN:
        game_state = "playing"
