from math import sqrt
from functools import reduce

class A_star():
    """to solve a matirx, invoke run method which returns a list of tuples with indexes of shortest path in order"""

    def __init__(self, matrix, start, finish):
        self.matrix = matrix
        self.values = [[{"f": 0, "g":0, "h":0, 'parent': None} for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        self.start = start
        self.finish = finish

    def distance(self, a, b):
        x = a[0] - b[0]
        y = a[1] - b[1]
        return sqrt(x**2 + y**2)

    def get_successors_of(self, cell):
        successors = []
        try:
            if cell[0]-1 >= 0:
                successors.append((cell[0]-1, cell[1]))
            if cell[1]-1 >= 0:
                successors.append((cell[0], cell[1]-1))
            if cell[1]+1 < len(self.matrix[0]):
                successors.append((cell[0], cell[1]+1))
            if cell[0]+1 < len(self.matrix):
                successors.append((cell[0]+1, cell[1]))
        except IndexError:
            pass
        #remove walls
        successors = list(filter(lambda x: self.matrix[x[0]][x[1]] == 1, successors))
        
        return successors

    def traceback(self, path, cell):
        if cell == self.start:# or cell is None:
            return
        path.append(cell)
        self.traceback(path, self.values[cell[0]][cell[1]]["parent"])


    def run(self):
        open_list = []
        closed_list = []
        self.values[self.start[0]][self.start[1]]["h"] = self.distance(self.start, self.finish)
        self.values[self.start[0]][self.start[1]]["f"] = self.values[self.start[0]][self.start[1]]["h"]
        open_list.append(self.start)
        found = False
        while len(open_list) != 0 and not found:
            
            q = reduce(lambda smallest, current: current if self.values[current[0]][current[1]]["f"] < self.values[smallest[0]][smallest[1]]["f"] else smallest, open_list)
            open_list.remove(q)
            successors = self.get_successors_of(q)

            for successor in successors:

                if successor == self.finish:
                    found = True
                    break

                current_g = self.values[q[0]][q[1]]["g"] + 1
                current_h = self.distance(self.finish, successor)
                current_f = current_g + current_h

                if successor in open_list and self.values[successor[0]][successor[1]]["f"] <= current_f:
                    continue

                if successor in closed_list and self.values[successor[0]][successor[1]]["f"] <= current_f:
                    continue

                self.values[successor[0]][successor[1]]["f"] = current_f
                self.values[successor[0]][successor[1]]["h"] = current_h
                self.values[successor[0]][successor[1]]["g"] = current_g

                self.values[successor[0]][successor[1]]["parent"] = q
                open_list.append(successor)

            closed_list.append(q)
        path = []
        self.traceback(path, closed_list[-1])
        return path