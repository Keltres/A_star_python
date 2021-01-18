"""A star in a maze"""
from matplotlib import pyplot as plt
from utils.Maze import Maze
from utils.astar_search import A_star

SIZE = 51
# 1 - path
# 0 - wall

maze = Maze(SIZE)

path = A_star(maze.matrix, maze.start, maze.finish).run()

for cell in path:
    maze.matrix[cell[0]][cell[1]] = 2

plt.pcolormesh(maze.matrix)

plt.show()
