"""pip install git+https://github.com/QuirkyCort/pgzhelper"""
import pgzrun
from pgzhelper import *
from random import randint
import time


# tamaño de pagina
WIDTH = 800
HEIGHT = 600

chico =Actor( 'chavo1')
chico.images = ['chavo1','chavo2','chavo3']
chico.fps = 5

def draw():
    screen.clear()
    chico.draw()
    

def update():
    chico.animate()
    """if keyboard.w:
        chico.y -= 5
    elif keyboard.s:
        chico.y += 5
    elif keyboard.a:
        chico.x -= 5
        chico.flip_x = True

    elif keyboard.d:
        chico.x += 5
        chico.flip_x = False


    if chico.x >523:
        chico.x = 523
    if chico.x <1:
        chico.x = 1
    if chico.y > 307:
        chico.y = 307
    if chico.y <1:
        chico.y = 1"""

def new_func():
    chico.animate()
    
pgzrun.go()