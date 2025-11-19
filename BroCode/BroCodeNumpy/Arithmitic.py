import numpy as np

#Scalar Arithmetic

array = np.array([1,2,3])

print(array+1) # each array element is added by 1 # can +, - *, / , **

#Vectorized math functions

arrayVector = np.array([1,2,3])

sqrt = (np.sqrt(arrayVector))
rounded = np.round(array)

roundDown = np.floor(arrayVector)
roundUp = np.ceil(arrayVector)
pi_variable = np.pi

radius = np.array([1,2,3])

# find area of circle

#print(np.pi * radius ** 2


      #Element Wise arithmetic)

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2) # [5 7 9]   can +, - *, / , **

#Comparrison operators

scores = np.array([91,55, 100, 73, 82,64])

scores[scores < 60] = 0
#print(scores == 100) #[False False  True False False False]

#------ BROADCASTING------# (Allows numpy to perform operations on arrays with different shapes by virtually
# expanding dimensions so they math larger array sizes)
#Dimmensions have same size OR pne has dimensions  size of  1


array3 = np.array