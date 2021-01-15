from math import pi
from random import randint, shuffle
from matplotlib import pyplot as plt
import numpy as np

size = 51
# 1 - path
# 0 - wall
matrix = [[1 if x%2 == 1 else 0 for x in range(size)] if y%2 == 1 else [0 for _ in range(size)] for y in range(size)]
matrix[0][1] = 1
matrix[50][1] = 1

walls = []
regions = []

for row in range(size):
    for column in range(size):
        if matrix[row][column] == 1:
            regions.append([(row, column)])
            

for row in range(1, size-1, 2):
    for element in range(2, size-2, 2):
            walls.append((row, element))
            walls.append((element, row))

shuffle(walls)
# print(walls)


for wall in walls:
    N = wall[0]+1
    S = wall[0]-1
    W = wall[1]-1
    E = wall[1]+1
    if (matrix[S][wall[1]] == 1 and matrix[N][wall[1]] == 1):
        matrix[wall[0]][wall[1]] = 1
        


    elif (matrix[wall[0]][W] == 1 and matrix[wall[0]][E] == 1):
        matrix.remove(wall)


plt.pcolormesh(matrix)

plt.show()
