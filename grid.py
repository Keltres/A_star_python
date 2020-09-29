"""grid class"""
from math import sqrt
import pygame
from tiles import Tile

class Grid():
    """class representing the gird of tiles"""
    def __init__(self, number_of_nodes, block_size, screen):
        self.drag = False
        self.start_drag_tile = None
        self._test_state = None
        self.tiles = []
        self._initialize_empty_list(number_of_nodes, block_size, screen)
        self.start_node = self.tiles[0][0].makeStart()
        self.finish_node = self.tiles[0][1].makeFinish()

    def _initialize_empty_list(self, number_of_nodes, block_size, screen):
        """a helper method; returns an array of (size number of nodes)x(size number of nodes) of normal nodes"""
        self.tiles = []
        for i in range(number_of_nodes):
            row = []
            for j in range(number_of_nodes):
                block = Tile((i*(block_size+2)+1,j*(block_size+2)+1), (block_size, block_size), screen)
                row.append(block)
                pygame.draw.rect(screen, Tile.TILE_COLOUR, block)
            self.tiles.append(row)

    def update_grid_list(self):
        """returns sorted grid"""
        new_grid = []
        flat_grid = []
        for row in self.tiles:
            for element in row:
                flat_grid.append(element)

        flat_grid.sort(key=lambda element: element.x)
        for _ in range(len(self.tiles)):
            row = []
            for _ in range(len(self.tiles[0])):
                row.append(flat_grid.pop(0))
            row.sort(key=lambda element:element.y)
            new_grid.append(row)
        self.tiles = new_grid

    def getSuccessorsOf(self, node):
        successors = []
        node.position = self.index_2d(node)
        try:
            successors.append(self.tiles[node.position[0]-1][node.position[1]])
            successors.append(self.tiles[node.position[0]][node.position[1]-1])
            successors.append(self.tiles[node.position[0]][node.position[1]+1])
            successors.append(self.tiles[node.position[0]+1][node.position[1]])
        except IndexError:
            pass

        #remove walls
        successors = list(filter(lambda x: x.state != "walls", successors))
        
        #change to paths
        for x in successors:
            x.parent = node
        return successors
        
    def set_drag_start_tile(self, mouse_pos):
        for row in self.tiles:
            for element in row:
                if element.collidepoint(mouse_pos):
                    self.start_drag_tile = element
                    self._test_state = element.state

    def set_drag(self, value):
        self.drag = value

    def drag_drawing(self, mouse_pos):
        for row in self.tiles:
            for element in row:
                if element.collidepoint(mouse_pos):
                    # case1: starting at normal, drawing through wall
                    if self._test_state == "normal" and element.state != "start" and element.state != "finish":
                        element.makeWall()

                    # case2: starting at wall, drawing through normal (erasing)
                    elif (self._test_state == "wall" or self._test_state == "path") and element.state != "start" and element.state != "finish":
                        element.makeNormal()

                    # case3: moving the start and finish tiles
                    elif self._test_state == "start" or self._test_state == "finish":
                        if element.state == "normal":
                            self.start_drag_tile.swtichTile(element)

    def index_2d(self, element):
        for i, x in enumerate(self.tiles):
            if element in x:
                return (i, x.index(element))
        return(None)

    def distance(self, a, b):
        x = self.index_2d(a)[0] - self.index_2d(b)[0]
        y = self.index_2d(a)[1] - self.index_2d(b)[1]
        return sqrt(x**2 + y**2)