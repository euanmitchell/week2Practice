import numpy as np
import mainTest                     # This is a Python script in the same directory

data=np.random.rand(50)

mean=mainTest.getMean(data)         # getMean() is a function defined in mainTest

print(data)
print("Mean is",mean)
