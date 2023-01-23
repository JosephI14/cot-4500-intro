import numpy as np

array = np.array([[0,0,0],[0,0,0], [0,0,0]])

for a in range(0,3):
    for b in range(0,3):
        if a == b:
            array[a][b] = 1
        else:
            array[a][b] = 0
print(array, end="\n\n")
for a in range(0,3):
    for b in range(0,3):
        if a != b:
            array[a][b] = 3
print(array, end="\n\n")
array = np.delete(array, 2,1)
print(array)
