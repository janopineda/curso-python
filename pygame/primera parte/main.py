import pygame
import variables
from jugador import Jugador1

chanito=Jugador1( 50 , 50)
pygame.init()



root =pygame.display.set_mode((variables.ancho,variables.alto))
pygame.display.set_caption("Juego de ")

m_arriba=False
m_derecha=False
m_izquierda=False
m_abajo=False

reloj=pygame.time.Clock()

#inicialización de la ventana
run= True
while run == True:
    
    reloj.tick(60)
    
    root.fill((0,0,20))
    
    delta_x=0
    delta_y=0
    
    if m_derecha == True:
        delta_x= 5
    if m_izquierda == True:
        delta_x= -5
    if m_arriba == True:
        delta_y= -5
    if m_abajo == True:
        delta_y= 5
    
    chanito.movimiento(delta_x , delta_y )
    
    chanito.colocar(root)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                m_izquierda = True
            if event.key == pygame.K_d:
                m_derecha=True
            if event.key == pygame.K_w:
                m_arriba=True
            if event.key == pygame.K_s:
                m_abajo=True
                
        if event.type== pygame.KEYUP:
            if event.key == pygame.K_a:
                m_izquierda = False
            if event.key == pygame.K_d:
                m_derecha=False
            if event.key == pygame.K_w:
                m_arriba=False
            if event.key == pygame.K_s:
                m_abajo=False
            
            
            
    pygame.display.update()
pygame.quit()