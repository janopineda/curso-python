"""pip install git+https://github.com/QuirkyCort/pgzhelper"""
import pgzrun
from pgzhelper import *
import sys
from random import randint



# tamaño de pagina
WIDTH = 800
HEIGHT = 600

chico =Actor( 'chavo1')
chico.images = ['chavo1','chavo2','chavo3']
chico.fps = 7

music.play('rola2')

fondo=Actor('fondo')

def draw():
    screen.clear()
    fondo.draw()
    chico.draw()
    

def update():
    movimiento_chico()
    limite_chico()

def limite_chico():
    
    if chico.x >800:
        chico.x = 800
    if chico.x <1:
        chico.x = 1
    if chico.y > 600:
        chico.y = 600   
    if chico.y <1:
        chico.y = 1

def movimiento_chico():
    chico.image="chavo1"
    chico.image="chavo2"
    if keyboard.w:
        chico.y -= 2
        chico.animate()

    elif keyboard.s:
        chico.y += 2
        chico.animate()

    elif keyboard.a:
        chico.x -= 2
        chico.animate()
        chico.flip_x = True

    elif keyboard.d:
        chico.x += 2
        chico.animate()
        chico.flip_x = False



    
pgzrun.go()
