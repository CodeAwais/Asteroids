import pygame
from constants import *
from player import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return       # makes the close button work

		screen.fill("black")    #Fill screen with a solid black color

		player.draw(screen)
		player.update(dt)
		
		pygame.display.flip()   #Refresh screen

		dt = clock.tick(60) / 1000 # sets game to 60 FPS and calculates time in seconds since last frame

if __name__ == "__main__":
    main()

