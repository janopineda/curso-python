import pgzrun
from pgzhelper import *
from random import randint


# tamaño de pagina
WIDTH = 524
HEIGHT = 307


pelota=True
velocidad=2
score1 = 0
score2 = 0
sonidoInicio=True
start=False
randon=randint(1,2)

bg =Actor( 'fondo')

botonStart=Actor('boton')


jugadorRojo =Actor( 'jugadoruno')
jugadorRojo.pos = 20, 307/2

jugadorVerde =Actor( 'jugadordos')
jugadorVerde.pos = 508, 307/2

balon=Actor('balon')
balon.pos= 524/2 , 307/2

MarcaGolizq=Actor('marcagol')
MarcaGolizq.pos= 1 , 156

MarcaGolDer=Actor('marcagol')
MarcaGolDer.pos= 521 , 156

music.play('rola2')
music.set_volume(.3)

def draw():
    screen.clear()
    bg.draw()
    screen.draw.text('Puntos: ' + str(score1) + ' / ' + str(score2), (15,10), color=(255,255,255), fontsize=30)
    MarcaGolDer.draw()
    MarcaGolizq.draw()
    jugadorRojo.draw()
    jugadorVerde.draw()
    balon.draw()
    botonStart.draw()

    

def update():
    global pelota
    global randon
    global velocidad
    global score2
    global score1
    global sonidoInicio
    global start

    if start == True:
        if sonidoInicio==True:
            sonido()

        if pelota == True:
            balon.x += velocidad
            balon.y -= randon

        if pelota == False:
            balon.x -= velocidad
            balon.y -= randon
            
        if balon.x > 523 :
            pelota = False
            balon.x = 520
            sounds.rebote.play()
        if balon.x < 0:
            pelota = True
            balon.x=10
            sounds.rebote.play()

        if balon.y < 0:
            balon.y =10
            randon = -abs(randon)
            sounds.rebote.play()

        if balon.y >307 :
            balon.y =307
            randon = +abs(randon)
            sounds.rebote.play()


        if keyboard.w:
            jugadorRojo.y -= 5
        elif keyboard.s:
            jugadorRojo.y += 5

        if keyboard.UP:
            jugadorVerde.y -= 5
        elif keyboard.DOWN:
            jugadorVerde.y += 5

        if jugadorRojo.x >523:
            jugadorRojo.x = 523
        if jugadorRojo.x <1:
            jugadorRojo.x = 1
        if jugadorRojo.y > 307:
            jugadorRojo.y = 307
        if jugadorRojo.y <1:
            jugadorRojo.y = 1
        
        if jugadorVerde.x >523:
            jugadorVerde.x = 523
        if jugadorVerde.x <1:
            jugadorVerde.x = 1
        if jugadorVerde.y > 307:
            jugadorVerde.y = 307
        if jugadorVerde.y <1:
            jugadorVerde.y = 1

        if jugadorRojo.colliderect(balon):
            pelota=True
            sounds.rebote.play()
            if velocidad < 14 :
                velocidad=velocidad+.4
                print(velocidad)

        if jugadorVerde.colliderect(balon):
            pelota=False
            sounds.rebote.play()
            if velocidad < 14 :
                velocidad=velocidad+.4
                print(velocidad)
        if score1==5 or score2==5:
            start=False
        if MarcaGolizq.colliderect(balon):
            balon.pos= 524/2 , 307/2
            velocidad=1
            score1 += 1
            pelota=True
            sounds.muerte.play()

        if MarcaGolDer.colliderect(balon):
            balon.pos= 524/2 , 307/2
            velocidad=1
            score2 += 1
            pelota=False
            sounds.muerte.play()
    elif start==False:
        score1=0
        score2 =0
        botonStart.pos= 524/2 , 307/2

def sonido():
    global sonidoInicio
    sounds.inicio.play()
    sonidoInicio=False

def on_mouse_down(pos):
    global start
    if botonStart.collidepoint(pos):
        start=True
        botonStart.pos= -100 , -100

pgzrun.go()