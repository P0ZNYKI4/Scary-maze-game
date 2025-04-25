import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

coord_x, coord_y = 0, 0
background = pygame.Surface((0, 0))

def load_new_level(number):
	spaw_point = {
		1: (110, 560),
		2: (758, 34),
		3: (80, 500)
	}

	global background
	background = pygame.image.load(f"level_{number}.png").convert()

	coord_x, coord_y = spaw_point[number]
	pygame.mouse.set_pos((coord_x, coord_y))

wall = pygame.Color((34, 32, 52, 255))
finish = pygame.Color((172, 50, 50, 255))

screamer = pygame.image.load("screamer.png").convert()
sound = pygame.mixer.Sound("screamer.mp3")

level_now = 1
load_new_level(level_now)

loop = 1
while loop:

	clock.tick(60)

	coord_x, coord_y = pygame.mouse.get_pos()

	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			loop = 0

	screen.blit(background, (0, 0))

	for i in range(5):

		color = screen.get_at((coord_x + i, coord_y + i))

		if color == wall:
			#level_now = 1
			load_new_level(level_now)
			break
		elif color == finish:
			level_now += 1
			load_new_level(level_now)
			break
	
	if level_now == 3 and coord_y <= 125:
		screen.blit(screamer, (0, 0))
		sound.play()
		pygame.display.flip()
		pygame.time.delay(3000)
		break

	pygame.draw.rect(screen, (255, 0, 0), (coord_x, coord_y, 5, 5))

	pygame.display.flip()
