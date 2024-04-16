from turtle import color
import pygame

class Jugador1():
    def __init__(self,x,y,animacion):
        #parametros de imagen
        self.flip=False
        self.animacion=animacion
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        self.image=animacion[self.frame_index]
        self.image=animacion[0]
        #voltear la imagen cuando preciones la techa
        
        
        self.rectangulo=pygame.Rect(0,0,40,40)
        self.rectangulo.center= (x,y)
        
    def update(self):
        cooldown_animacion=500
        self.image=self.animacion[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >=cooldown_animacion:
            self.frame_index=self.frame_index +1 
            self.update_time=pygame.time.get_ticks()
        
    def movimiento(self , delta_x , delta_y):
        self.rectangulo.x = self.rectangulo.x + delta_x
        self.rectangulo.y = self.rectangulo.y + delta_y
        #colocar flip con if
        if delta_x < 0:
            self.flip=True
        if delta_x > 0:
            self.flip=False
        
    def colocar(self,interfaz):
        #cambiar flip
        image_flip=pygame.transform.flip(self.image,self.flip,False)
        #colocar la imagen en el rectangulo
        interfaz.blit(image_flip,self.rectangulo)
        
        #pygame.draw.rect(interfaz, (255, 255, 0) , self.rectangulo , width=1)