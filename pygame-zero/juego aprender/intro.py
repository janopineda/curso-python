"""pip install git+https://github.com/QuirkyCort/pgzhelper"""
import pgzrun
from pgzhelper import *

# tamaño de pagina
WIDTH = 800
HEIGHT = 600

casimiro = Actor('casimiro1')
casimiro.images = ['casimiro1', 'casimiro2']
casimiro.fps = 7  # Velocidad de animación (no se usa directamente aquí)

music.play('rola2')

fondo = Actor('fondo')

speed = 50
frame_counter = 0  # Contador de frames para controlar la animación

def draw():
    screen.clear()
    fondo.draw()
    casimiro.draw()

def update():
    limite_casimiro()
    movimiento_chico()

def limite_casimiro():
    if casimiro.x > 800:
        casimiro.x = 800
    if casimiro.x < 1:
        casimiro.x = 1
    if casimiro.y > 600:
        casimiro.y = 600
    if casimiro.y < 1:
        casimiro.y = 1

def movimiento_chico():
    global frame_counter
    frame_counter += 1  

    if keyboard.a:
        casimiro.x -= 2
        casimiro.flip_x = True
        if frame_counter % 10 == 0:  
            casimiro.next_image()

    elif keyboard.d:
        casimiro.x += 2
        casimiro.flip_x = False
        if frame_counter % 10 == 0:  
            casimiro.next_image()

pgzrun.go()
   
  