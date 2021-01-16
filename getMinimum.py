'''
A Python script to import the 'minimum' function from findMinimum.py
and call it on some data.
'''

import numpy as np
import findMinimum

testData=np.random.rand(100)

testMin=findMinimum.minimum(testData)
print("The minimum value is",testMin)
