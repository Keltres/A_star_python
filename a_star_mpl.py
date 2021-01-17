from matplotlib import pyplot as plt
import numpy as np
from a_start_mpl.Maze import Maze

SIZE = 13
# 1 - path
# 0 - wall
        
maze = Maze(SIZE)

plt.pcolormesh(maze.matrix)

plt.show()
