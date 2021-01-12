"""grid class"""
import pygame
from astarpygame.tiles import Tile

class Grid():
    """class representing the gird of tiles"""
    def __init__(self, number_of_nodes, block_size, screen):
        self.tiles = []
        self._initialize_empty_list(number_of_nodes, block_size, screen)
        self.number_of_nodes = number_of_nodes
        self.start_node = None
        self.finish_node = None

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

    def getSuccessorsOf(self, node):
        successors = []
        node.position = self.index_2d(node)
        try:
            if node.position[0]-1 >= 0:
                successors.append(self.tiles[node.position[0]-1][node.position[1]])
            if node.position[1]-1 >= 0:
                successors.append(self.tiles[node.position[0]][node.position[1]-1])
            if node.position[1]+1 < self.number_of_nodes:
                successors.append(self.tiles[node.position[0]][node.position[1]+1])
            if node.position[0]+1 < self.number_of_nodes:
                successors.append(self.tiles[node.position[0]+1][node.position[1]])
        except IndexError:
            pass

        #remove walls
        successors = list(filter(lambda x: x.state != "wall", successors))
        
        #change to paths
        # for x in successors:
        #     x.parent = node
        return successors

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
                                current.state == "path"
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
                                previous.state == "path"
                                ) 
                                and current.state == "wall"
                            ) 
                            or (previous is not None and previous.state == "normal" and current.state == "path")
                        ):
                        current.makeNormal()
                        return current

                    # case3: moving the start and finish tiles
                    elif (previous is None and
                    (current.state == "start" or current.state == "finish")):
                        return current
                    elif (current.state == "path" or current.state == "normal"):
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

    def distance(self, a, b):
        x = self.index_2d(a)[0] - self.index_2d(b)[0]
        y = self.index_2d(a)[1] - self.index_2d(b)[1]
        # return sqrt(x**2 + y**2)
        return abs(x)+abs(y)

    def cleanup(self, v = 0):
        """cleans the grid of paths (and walls if v is anthing other than 0)"""
        for row in self.tiles:
            for element in row:
                if v != 0:
                    if element.state == "wall":
                        element.makeNormal()
                if element.state == "path":
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
