import pgzrun
from random import randint


# tamaño de pagina
WIDTH = 524
HEIGHT = 307


pelota=True
randon=randint(3,8)

bg =Actor( 'fondo')

jugadorRojo =Actor( 'jugadoruno')
jugadorRojo.pos = 10, 307/2

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


    if pelota == True:
        balon.x += 2
        balon.y -= randon
    if pelota == False:
        balon.x -= 2
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


    

    if keyboard.a: 
        jugadorRojo.x -= 10
    elif keyboard.d:
        jugadorRojo.x += 10
    elif keyboard.w:
        jugadorRojo.y -= 10
    elif keyboard.s:
        jugadorRojo.y += 10

    if jugadorRojo.x >523:
        jugadorRojo.x = 523
    if jugadorRojo.x <1:
        jugadorRojo.x = 1
    if jugadorRojo.y > 307:
        jugadorRojo.y = 307
    if jugadorRojo.y <1:
        jugadorRojo.y = 1

    if jugadorRojo.colliderect(balon):
        print("pasomecha")
        

pgzrun.go()