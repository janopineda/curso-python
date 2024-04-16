from turtle import color
import pygame

class Jugador1():
    def __init__(self,x,y):
        self.rectangulo=pygame.Rect(0,0,40,40)
        self.rectangulo.center= (x,y)
        
    def movimiento(self , delta_x , delta_y):
        self.rectangulo.x = self.rectangulo.x + delta_x
        self.rectangulo.y = self.rectangulo.y + delta_y
        
    def colocar(self,interfaz):
        pygame.draw.rect(interfaz, (255, 255, 0) , self.rectangulo )