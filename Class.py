import pygame
from pygame.locals import *

AllJugador = pygame.sprite.Group()
pygame.mixer.init()
Effect = pygame.mixer.Sound("C:\Programas de Pyhon\ProgramasPractica\Practica_Dia_21\Resumen Clases\Effect.wav")

def cargar_imagen_t(filename):
    im = pygame.image.load(filename)        
    im = im.convert()
    color = im.get_at((0,0))
    im.set_colorkey(color, RLEACCEL)
    return im

class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.v = pygame.Vector2()
        self.v.xy = 0,-7
        self.image = cargar_imagen_t("C:\Programas de Pyhon\ProgramasPractica\Practica_Dia_21\Resumen Clases\Player.png")
        # Cambiar los archivos de carga de las imagenes.
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400
    def update(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP] and self.rect.top>0:
            self.rect.top -= 10
        if tecla[pygame.K_DOWN] and self.rect.bottom < 700:
            self.rect.bottom += 10
        if tecla[pygame.K_LEFT] and self.rect.left>0:
            self.rect.left -= 10
        if tecla[pygame.K_RIGHT] and self.rect.right<700:
            self.rect.right += 10

def Level(screen):
    pygame.init
    pygame.display.set_caption("La pasta que se mueve por el escenario.")
    Background = pygame.image.load("C:\Programas de Pyhon\ProgramasPractica\Practica_Dia_21\Resumen Clases\Background.png")
    # Cambiar los archivos de carga de las imagenes.
    Background = pygame.transform.scale(Background,(800,800))
    Pasta_Player = Player()
    AllJugador.add(Pasta_Player)
    Correr = True
    Reloj = pygame.time.Clock()
    while Correr:
        Reloj.tick(60)
        screen.blit(Background,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                Correr = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:                   
                Effect.play()
        AllJugador.update()
        AllJugador.draw(screen)
        pygame.display.flip()
    pygame.quit