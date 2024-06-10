"""
Libreria para pgzhelper
pip install git+https://github.com/QuirkyCort/pgzhelper
pip install pgzero

"""
import pgzrun
from pgzhelper import *
import os


fondo=Actor('fondo')
fondo.images = ['fondo','fondo2']

boton1=Actor('boton')
boton1.pos = 800/3, 600/2
#boton1.opacity=0.1


boton2=Actor('boton')
boton2.pos = 800/1.5, 600/2

boton3=Actor('miau')
boton3.pos = -200, 0

def draw():
    screen.clear()
    fondo.draw()
    boton1.draw()
    boton2.draw()
    boton3.draw()


def update():
    boton2.x += 2
    print("hola")
    #fondo.animate()
    

def on_mouse_down(pos):
    global Translado
    if boton1.collidepoint(pos):
        fondo.image='fondo2'
        boton1.pos = -200, 0
        boton2.pos = -200, 0
        sounds.cat.play()
        boton3.pos = 800/2, 600/2
    else:
        print("hey man nooo")

"""os.environ['SDL_VIDEO_CENTERED'] = '1' # centrar pantalla"""
pgzrun.go()
