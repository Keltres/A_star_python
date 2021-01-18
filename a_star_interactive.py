"""bla bla bla"""
import sys
import concurrent.futures

import pygame
# from astarpygame.functions import start_algorithm, draw_path
from utils.grid import Grid
from utils.astar_search import A_star
#import tiles

NUMBER_OF_BLOCKS = 32
BLOCK_SIZE = 18
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
        clock.tick(300)
        # events handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # reset drag drawing
            if event.type == pygame.MOUSEBUTTONUP:
                element = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    # with concurrent.futures.ThreadPoolExecutor() as executor:
                    #     astar = A_star(grid.cellular(), grid.index_2d(grid.start_node), grid.index_2d(grid.finish_node))
                    #     future = executor.submit(astar.run())
                    #     path = future.result()
                    grid.cleanup()
                    astar = A_star(grid.cellular(), grid.index_2d(grid.start_node), grid.index_2d(grid.finish_node))
                    path = astar.run()
                    if len(path) > 0:
                        grid.draw_path(path)
                    else:
                        print("Path not found")
                    del(astar)
                elif event.key == pygame.K_c:
                    grid.cleanup(1)

        # handling of a drag-drawing
        if pygame.mouse.get_pressed()[0]:
            element = grid.drag_drawing(pygame.mouse.get_pos(), element)

        pygame.display.flip()


if __name__ == "__main__":
    main()
    