import pygame 
import random 
import math 
import sys 
import os

#inicializar pygame
pygame.init()

#establece el tamaño de la pantalla
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))

#funcion para obtener la ruta de los recursos 
def resource_path(relative_paht):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_paht)    

#cargar imagen de fondo 
asset_backgroudn = resource_path("assets/images/backgrond.png")
background = pygame.image.load(asset_backgroudn)

#cargar icono de ventana 
asset_icon = resource_path("assets/images/ufo.png")
icon = pygame.image.load(asset_icon)  

#cargar cargar sonido de fondo
asset_sound = resource_path("assets/audio/backgraound_music.mp3")
background_sound = pygame.mixer.music.load(asset_sound)  


#cargar imagen del jugador
asset_playerimg = resource_path("assets/images/space-invaders.png")
playerimg = pygame.image.load(asset_playerimg)  

#cargar imagen de bala 
asset_bulletimg = resource_path("assets/images/bullet.png")
bulletimg = pygame.image.load(asset_bulletimg)  

#cargar fuente para texto de game over
asset_over_font = resource_path("assets/fonts/RAIVE.TTF")
over_font = pygame.font.FONT(asset_bulletimg)  

#cargar fuente de texto de puntuaje 
asset_font = resource_path("assets/fonts/commibd.ttf")
font = pygame.font.FONT(asset_font)  
 
 #establecer titulo de ventana
pygame.display.setcaption("Astrobot")

#establecer icono de ventana 
pygame.display.set_icon(icon)