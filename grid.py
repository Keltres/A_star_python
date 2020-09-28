"""grid class"""
from copy import deepcopy
from tiles import Tile

class Grid():
    """class representing the gird of tiles"""
    def __init__(self, number_of_nodes, block_size):
        self.tiles = self.get_empty_grid(number_of_nodes, block_size)
        self.start_node = self.tiles[0][0].makeStart()
        self.finish_node = self.tiles[0][1].makeFinish()

    def get_empty_grid(self, number_of_nodes, block_size):
        """returns an array of (size number of nodes)x(size number of nodes) of normal nodes"""
        blocks = []
        for i in range(number_of_nodes):
            row = []
            for j in range(number_of_nodes):
                block = Tile((i*(block_size+2)+1,j*(block_size+2)+1), (block_size, block_size))
                row.append(block)
            blocks.append(row)
        return blocks

    def update_grid_list(self):
        """returns sorted grid"""
        new_grid = []
        flat_grid = []
        for row in self.tiles:
            for element in row:
                flat_grid.append(element)

        flat_grid.sort(key=lambda element: element.x)
        for j in range(len(self.tiles)):
            row = []
            for i in range(len(self.tiles[0])):
                row.append(flat_grid.pop(0))
            row.sort(key=lambda element:element.y)
            new_grid.append(row)
        self.tiles = new_grid

    def getNeighbourOf(self, node):
        pass