import pygame
pygame.init()
screen = pygame.display.set_mode((600,700))
bg = pygame.image.load('./images/background.png') 
screen.blit(bg,(1,3))
hero = pygame.image.load('./images/hero.gif')
screen.blit(hero,(50,100))
hero_rect = pygame.Rect(150,500,102,126)
clock = pygame.time.Clock()
i = 0
while True:
	clock.tick(30)
	hero_rect.y-=1
	hero_rect.x+=1
	if hero_rect.y <= 0:
		hero_rect.y = 700
	elif hero_rect.x >= 3:
		hero_rect.x = 500
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
	i+=1
pygame.quit()
