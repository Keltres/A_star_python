"""bla bla bla"""
import sys

import pygame
from functions import start_algorithm
from functions import draw_path
from grid import Grid
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


while True:
    clock.tick(45)
    # events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.set_drag(True)
            grid.set_drag_start_tile(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            grid.set_drag(False)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                grid.cleanup()
                path = start_algorithm(grid)
                draw_path(path[-1])
            elif event.key == pygame.K_c:
                grid.cleanup(1)


    # handling of a drag-drawing
    if grid.drag:
        grid.drag_drawing(pygame.mouse.get_pos())
        grid.update_grid_list()

    pygame.display.flip()
