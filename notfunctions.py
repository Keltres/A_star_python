"""functions for a* search"""
from functools import reduce

def start_algorithm(grid):
    open_list = []
    closed_list = []
    open_list.append(grid.start_node)
    found = False
    while len(open_list) != 0 and not found:

        # out of elements in OPEN list get the one with smallest f 
        q = reduce(lambda smallest, current: current if current.star_f <= smallest.star_f else smallest, open_list)
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
        
        closed_list.append(q)

    return closed_list

def draw_path(element):
    if element.state == "start":
        return
    element.makePath()
    draw_path(element.parent)