"""pip install git+https://github.com/QuirkyCort/pgzhelper"""
import pgzrun

#tamaño de pagina:
WEITH=950
HEIGHT=600

chico=Actor('casimiro')
chico.fps = 7
chico.pos = (200, 500)

fondo=Actor ('fondo')

def draw():
    screen.clear()
    fondo.draw()
    chico.draw()

def update():
    movimiento_chico()
    limite_chico()

def limite_chico():
    if chico.x >1000:
        chico.x = 1000
    if chico.x <1:
        chico.x = 1
    if chico.y > 600:
        chico.y = 600   
    if chico.y <1:
        chico.y = 1

def movimiento_chico():

    if keyboard.w:
        chico.y -= 2

    elif keyboard.s:
        chico.y += 2


    elif keyboard.a:
        chico.x -= 2
        chico.flip_x = True

    elif keyboard.d:
        chico.x += 2
        chico.flip_x = False

pgzrun.go()