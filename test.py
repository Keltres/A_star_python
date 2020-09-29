from copy import deepcopy

lista = [[1,2,3],[4,5,6],[7,8,9]]

gowno = deepcopy(lista)

gowno.append("kurwa")

print(gowno, lista)