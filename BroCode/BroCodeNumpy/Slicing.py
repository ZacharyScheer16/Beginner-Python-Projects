import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

# array[start: end: step]

countByTwo = (array[0:4:2]) # counting by 2 other way tow write array[::2 ]
reversedRow = array[::-1]
byTwoReversedOrder = array[::-2]

print(array[:,0]) # prints all rows accessed at column 0
print("\n")
print("\n")
print(array[:,0:3]) # prints first three columns
print("\n")
print("\n")
print(array[:,::-1]) #reverses order of arrays