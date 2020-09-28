"""bla bla bla"""
import sys

import pygame
from functions import *
#import tiles

pygame.init()
WIDTH = 640
HEIGHT = 640
BLOCK_SIZE = 38
NUMBER_OF_BLOCKS = WIDTH//(BLOCK_SIZE+2)
blocks = []

clock = pygame.time.Clock()

#FLAGS
flags = {
    "drag": False,
    "drag_start_tile_state": None,
    "drag_start_tile": None,
}

screen = pygame.display.set_mode((WIDTH, HEIGHT+80))
screen.fill((0,0,0))
grid = get_empty_grid(WIDTH, HEIGHT, BLOCK_SIZE)
# print(grid)
# grid[0][0].makeStart()
# grid[0][1].makeFinish()

for row in grid:
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
            set_drag_start_tile(grid, flags, pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            reset_falgs(flags)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                start_algorithm(grid)

    # handling of a drag-drawing
    if flags["drag"]:
        for row in grid:
            for element in row:
                update_labels(element, flags, pygame.mouse.get_pos())
                element.updateColour(screen)
        grid = update_grid_list(grid)

    pygame.display.flip()
