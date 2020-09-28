"""bla bla bla"""
import sys

import pygame
from functions import *
from grid import Grid
#import tiles

NUMBER_OF_BLOCKS = 16
BLOCK_SIZE = 38
HEIGHT = WIDTH = NUMBER_OF_BLOCKS*(BLOCK_SIZE+2)


#FLAGS
flags = {
    "drag": False,
    "drag_start_tile_state": None,
    "drag_start_tile": None,
}

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT+80))
screen.fill((0,0,0))
grid = Grid(NUMBER_OF_BLOCKS, BLOCK_SIZE)

# initalize grid on screen
for row in grid.tiles:
    for element in row:
        element.updateColour(screen)

while True:
    clock.tick(45)
    # events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            flags["drag"] = True
            set_drag_start_tile(grid.tiles, flags, pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            reset_falgs(flags)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                start_algorithm(grid.tiles)

    # handling of a drag-drawing
    if flags["drag"]:
        for row in grid.tiles:
            for element in row:
                if element.collidepoint(pygame.mouse.get_pos()):
                    update_labels(element, flags)
                element.updateColour(screen)

        grid.update_grid_list()

    pygame.display.flip()
