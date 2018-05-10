background_image_filename = 'timg.jpeg'
mouse_image_filename = 'u=3053898757,1196731043&fm=27&gp=0.jpg'

import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1200,797),0,32)
pygame.display.set_caption('Hello,World!')
background = pygame.image.load(background_image_filename).convert()
mouse_coursor = pygame.image.load(mouse_image_filename).convert_alpha()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background,(0,0))
	x,y = pygame.mouse.get_pos()
	x-=mouse_coursor.get_width()/2
	y-=mouse_coursor.get_height()/2
	screen.blit(mouse_coursor,(x,y))
	pygame.display.update()
