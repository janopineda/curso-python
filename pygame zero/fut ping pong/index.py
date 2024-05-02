import pgzrun
from pgzhelper import *
from random import randint


# tamaño de pagina
WIDTH = 524
HEIGHT = 307


pelota=True
velocidad=2
randon=randint(1,2)

bg =Actor( 'fondo')

jugadorRojo =Actor( 'jugadoruno')
jugadorRojo.pos = 20, 307/2

balon=Actor('balon')
balon.pos= 524/2 , 307/2



def draw():
    screen.clear()
    bg.draw()
    jugadorRojo.draw()
    balon.draw()

def update():
    global pelota
    global randon
    global velocidad


    if pelota == True:
        balon.x += velocidad
        balon.y -= randon
    if pelota == False:
        balon.x -= velocidad
        balon.y -= randon
        
    if balon.x > 523:
        pelota = False
        balon.x = 520
    if balon.x < 0:
        pelota = True
        balon.x=10

    if balon.y < 0:
        balon.y =10
        randon = -abs(randon)

    if balon.y > 307:
        balon.y =307
        randon = +abs(randon)


    if keyboard.w:
        jugadorRojo.y -= 5
    elif keyboard.s:
        jugadorRojo.y += 5

    if jugadorRojo.x >523:
        jugadorRojo.x = 523
    if jugadorRojo.x <1:
        jugadorRojo.x = 1
    if jugadorRojo.y > 307:
        jugadorRojo.y = 307
    if jugadorRojo.y <1:
        jugadorRojo.y = 1

    if jugadorRojo.colliderect(balon):
        pelota=True
        velocidad=velocidad+.8

pgzrun.go()