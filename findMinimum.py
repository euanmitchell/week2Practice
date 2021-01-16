'''
A script to define a minimum-finding function with a test case in the
main block. Will be imported and called in getMinimum.py
'''

import numpy as np

# Define the minimum function
def minimum(x):
    min = x[0]
    for i in range(len(x)):
        if x[i] < min:
            min=x[i]
        else:
            continue
    return min

# Call minimum() in the main block
if __name__ == '__main__':
    # Generate some random data
    data=np.random.rand(25)
    # Call minimum
    dataMin=minimum(data)
    print(data)
    print("Minimum value is",dataMin)
