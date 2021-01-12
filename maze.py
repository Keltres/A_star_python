import pygame
# from tiles import Tile 
from astarpygame.grid import Grid

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

def main():

    grid = Grid(NUMBER_OF_BLOCKS, BLOCK_SIZE, screen)
    while True:
        clock.tick(45)
        pygame.display.flip()

        
if __name__ == "__main__":
    main()