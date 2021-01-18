import sys

import pygame
# from tiles import Tile 
from utils.grid import Grid

def print_table(matrix):
    for row in matrix:
        print(row)

def make_maze(matrix):
    pass

NUMBER_OF_BLOCKS = 16
BLOCK_SIZE = 38
HEIGHT = WIDTH = NUMBER_OF_BLOCKS*(BLOCK_SIZE+2)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

grid = Grid(NUMBER_OF_BLOCKS, BLOCK_SIZE, screen)
grid.set_start((5, 10))
grid.set_finish((10, 5))

def main():

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
                if event.key == pygame.K_c:
                    grid.cleanup(1)

        # handling of a drag-drawing
        if pygame.mouse.get_pressed()[0]:
            element = grid.drag_drawing(pygame.mouse.get_pos(), element)

        pygame.display.flip()

        
if __name__ == "__main__":
    main()