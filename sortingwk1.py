# Problem = Sorting a random array of numbers from low to high
# Input = An array of random numbers
# Output = The input array sorted from lowest to highest

import time
import numpy as np
import findMinimum

t=time.clock()

testData=np.random.rand(100)

def sortArray(randArray):
    '''
    A function to sort a random array of any length
    into a new array ordered from low to high value.
    The minimum finding function is imported as
    minimum() from findMinimum.py.
    '''
    # Create container to hold sorted array and initialise with zeros
    sortedArray=np.zeros(len(randArray))
    # Loop through the array (i will start at 0 here)
    for i in range(len(randArray)):
        # Identify the minimum value in the random array and store to variable
        # by calling imported function minimum()
        newMin=findMinimum.minimum(randArray)
        # Set the ith index in the sorted array to the current minimum value
        sortedArray[i]=newMin
        # Remove the current minimum value from the random array
        randArray=np.delete(randArray, np.where(randArray==newMin))

    return sortedArray

sortedData = sortArray(testData)

print("Random array:",testData)
print("Sorted array:",sortedData)

t=time.clock() - t
print("Calculation Time: %0.12f seconds" % (t))
