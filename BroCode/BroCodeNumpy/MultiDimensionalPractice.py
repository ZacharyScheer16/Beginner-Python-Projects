
import numpy as np

array = np.array([[['A', 'B'], ['C', 'D'],['E', 'F']],
                  [['G', 'H'], ['I', 'J'],['K', 'L']],# needs consistent amount of elements in space
                  [['M', 'N'], ['O', 'P'],['Q', 'R']]]) # zero dimensional array ndim(number od dimensions in array)
print(array.ndim)
print(array.shape) # tuple of integer, shows depth (3, _ , _); number of rows (_, 3, _); and number of columns (_,_, 2)

print(array [0][0][0]) # chain indexing in normal python
print(array[2][1][0])#multidimensional in NUMPY

word = array[0,0,0] + array[0,1,0] + array[2,2,1]

print(word)
