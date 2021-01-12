"""bla bla bla"""
import sys

import pygame
from astarpygame.functions import start_algorithm, draw_path
from astarpygame.grid import Grid
#import tiles

NUMBER_OF_BLOCKS = 16
BLOCK_SIZE = 38
HEIGHT = WIDTH = NUMBER_OF_BLOCKS*(BLOCK_SIZE+2)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0,0,0))

# initalize grid on screen
grid = Grid(NUMBER_OF_BLOCKS, BLOCK_SIZE, screen)
grid.set_start((0, 0))
grid.set_finish((0, 1))

def main():
    """main"""
    element = None
    while True:
        clock.tick(45)
        # events handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # reset drag drawing
            if event.type == pygame.MOUSEBUTTONUP:
                element = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    path = start_algorithm(grid)
                    if len(path) > 0:
                        draw_path(path[-1])
                    else:
                        print("Path not found")
                elif event.key == pygame.K_c:
                    grid.cleanup(1)

        # handling of a drag-drawing
        if pygame.mouse.get_pressed()[0]:
            element = grid.drag_drawing(pygame.mouse.get_pos(), element)

        pygame.display.flip()


if __name__ == "__main__":
    main()
    