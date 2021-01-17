from random import shuffle

class Maze:

    def __init__(self, size):
        """Constructor for the Maze class; on initialization creates a square 2d array - a maze"""
        self.matrix = [[1 if x%2 == 1 else 0 for x in range(size)] if y%2 == 1 else [0 for _ in range(size)] for y in range(size)]
        self.walls = [] # list of tuples [(0,1), (2,3)]
        self.regions = [] # list of lists of tuples [[(0,1),(2,3)],[(4,5)]]
        self.matrix[size-1][1] = 1
        self.matrix[0][size-2] = 1
        self.size = size
        self.__main()

    def __fill_walls(self):
        """Helper method called at initialization"""
        for row in range(1, self.size-1, 2):
            for element in range(2, self.size-2, 2):
                self.walls.append((row, element))
                self.walls.append((element, row))

        shuffle(self.walls)

    def __fill_regions(self):
        """Helper method called at initialization"""
        for row in range(self.size):
            for column in range(self.size):
                if self.matrix[row][column] == 1:
                    self.regions.append(Region(first = [(row, column)]))

    def __find_region_of(self, element):
        for region in self.regions:
            if region.contain(element):
                return region

    def __maze_step(self, wall, c1, c2):
        """joins to regions if they are separated by the wall and adds the wall to that joined region"""
        H = wall[0]
        V = wall[1]
        r1 = self.__find_region_of(c1)                                  # find those regions of adjacent cells
        r2 = self.__find_region_of(c2)
        if not r1 is r2:                                                # if those regions are not the same one
            # self.walls.remove(wall)                                     # remove wall from walls
            self.matrix[H][V] = 1                                       # make this wall a path
            new_region = Region(r1.elements, r2.elements)               # make a new region out of previous two
            self.regions.remove(r1)                                     # remove previous two regions from regions list
            self.regions.remove(r2)
            new_region.add_to_region((H,V))                             # add this wall to the new region
            self.regions.append(new_region)                             # add new region to regions list

    def __make_maze(self):
        for wall in self.walls:
        # indexes of cells
            N = wall[0]+1
            S = wall[0]-1
            W = wall[1]+1
            E = wall[1]-1
            H = wall[0]
            V = wall[1]
            if (self.matrix[S][V] == 1 and self.matrix[N][V] == 1):
                self.__maze_step(wall, (S,V), (N,V))
            elif(self.matrix[H][E] == 1 and self.matrix[H][W] == 1):
                self.__maze_step(wall, (H,E), (H,W))

    def __main(self):
        self.__fill_walls()
        self.__fill_regions()
        self.__make_maze()



class Region:
    def __init__(self, first = [], second = []):
        self.elements = first + second

    def add_to_region(self, element):
        """adds a tuple to a region"""
        self.elements.append(element)

    def contain(self, element):
        """returns true if a region contains the element"""
        return element in self.elements

