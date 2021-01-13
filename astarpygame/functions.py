"""functions for a* search"""
import time
from functools import reduce
import pygame

def start_algorithm(grid):
    """a* algorithm returns an array of Tiles which are the shortest path from start to finish"""
    grid.cleanup()
    open_list = []
    closed_list = []
    grid.start_node.star_g = 0
    grid.start_node.star_h = grid.distance(grid.finish_node, grid.start_node)
    grid.start_node.star_f = grid.start_node.star_g + grid.start_node.star_h
    open_list.append(grid.start_node)
    found = False
    while len(open_list) != 0 and not found:

        # out of elements in OPEN list get the one with smallest f
        q = reduce(lambda smallest, current: current if current.star_f < smallest.star_f else smallest, open_list)
        # pop q out of the OPEN list
        open_list.pop(open_list.index(q))
        # get all successors of q
        q.successors = grid.getSuccessorsOf(q)

        for successor in q.successors:

            if successor == grid.finish_node:
                found = True
                break

            current_g = q.star_g + 1
            current_h = grid.distance(grid.finish_node, successor)
            current_f = current_g + current_h

            if successor in open_list and successor.star_f <= current_f:
                continue

            if successor in closed_list and successor.star_f <= current_f:
                continue

            successor.star_f = current_f
            successor.star_h = current_h
            successor.star_g = current_g

            successor.parent = q
            open_list.append(successor)


        if q.state != "start":
            q.makeSearch()
        closed_list.append(q)
        # time.sleep(0.005)
        pygame.display.flip()
    if not found:
        return []
    return closed_list

def draw_path(element):
    """draws the path from element to start"""
    if element.state == "start":
        return
    element.makePath()
    draw_path(element.parent)
