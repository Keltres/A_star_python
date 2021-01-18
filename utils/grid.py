"""grid class"""
import pygame
from utils.tiles import Tile

class Grid():
    """class representing the gird of tiles"""
    tiles = []
    start_node = None
    finish_node = None

    def __init__(self, number_of_nodes, block_size, screen):
        self._initialize_empty_list(number_of_nodes, block_size, screen)
        self.number_of_nodes = number_of_nodes
        

    def _initialize_empty_list(self, number_of_nodes, block_size, screen):
        """a helper method; returns an array of (size number of nodes)x(size number of nodes) of normal nodes"""
        self.tiles = []
        for i in range(number_of_nodes):
            row = []
            for j in range(number_of_nodes):
                block = Tile((j*(block_size+2)+1,i*(block_size+2)+1), (block_size, block_size), screen)
                row.append(block)
                pygame.draw.rect(screen, Tile.TILE_COLOUR, block)
            self.tiles.append(row)

    def drag_drawing(self, mouse_pos, previous):
        """handles drawing of tiles with mouse drag
        previous argument is where mouse has been before the current tile or null if just pressing mouse"""
        for row in self.tiles:                                              # \
            for current in row:                                             #  > this gets the element the mouse is on -> current element
                if current.collidepoint(mouse_pos) and current != previous: # /
                    # case1: drawing a wall
                    if (
                            (
                                previous is None or
                                previous.state == "wall"
                            )
                            and
                            (
                                current.state == "normal" or
                                current.state == "path" or
                                current.state == "search"
                            )
                        ):
                        current.makeWall()
                        return current

                    # case2: ereasing walls
                    elif (
                            (
                                (
                                previous is None or
                                previous.state == "normal" or
                                previous.state == "path" or 
                                previous.state == "search"
                                ) 
                                and current.state == "wall"
                            ) 
                            or (previous is not None and 
                                previous.state == "normal" 
                            and (current.state == "path" or current.state == "search"))
                        ):
                        current.makeNormal()
                        return current

                    # case3: moving the start and finish tiles
                    elif (previous is None and
                    (current.state == "start" or current.state == "finish")):
                        return current
                    elif (current.state == "path" or current.state == "search" or current.state == "normal"):
                        if(previous.state == "start"):
                            current.makeStart()
                            self.set_start(current)
                            previous.makeNormal()
                        elif(previous.state == "finish"):
                            current.makeFinish()
                            self.set_finish(current)
                            previous.makeNormal()
                        return current

                    # in all other cases "skip"
                    else:
                        return previous

        return previous

    def index_2d(self, element):
        for i, x in enumerate(self.tiles):
            if element in x:
                return (i, x.index(element))
        return(None)

    def cleanup(self, v = 0):
        """cleans the grid of paths (and walls if v is anthing other than 0)"""
        for row in self.tiles:
            for element in row:
                if v != 0:
                    if element.state == "wall":
                        element.makeNormal()
                if element.state == "path" or element.state == "search":
                    element.makeNormal()

    def set_start(self, node):
        if isinstance(node, Tile):
            self.start_node = node
        elif isinstance(node, tuple):
            self.start_node = self.tiles[node[0]][node[1]].makeStart()

    def set_finish(self, node):
        if isinstance(node, Tile):
            self.finish_node = node
        elif isinstance(node, tuple):
            self.finish_node = self.tiles[node[0]][node[1]].makeFinish()

    def draw_path(self, path):
        for element in path:
            self.tiles[element[0]][element[1]].makePath()

    def cellular(self):
        cells = []
        for row in self.tiles:
            new_row = []
            for cell in row:
                if cell.state == "wall":
                    new_row.append(0)
                else:
                    new_row.append(1)
            cells.append(new_row)
        return cells