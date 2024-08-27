# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return       # makes the close button work	


		screen.fill((0,0,0))    #Fill screen with a solid black color
		pygame.display.flip()   #Refresh screen
		
			


	print("Starting asteroids!")

	print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
