import numpy as np
import matplotlib.pyplot as plt
import pylab

range1 = [1,2,3]
range2 = np.linspace(1,3,num=3)
print(range2)

print("Results 1:")
result = []
for i in range(len(range1)):
    result.append(pow(range1[i],3))
    print("V",i,"=",result[i],sep='')

print("Results 2:")
result2 = []
for i in range(len(range2)):
    result2.append(pow(range2[i],3))
    print("V",i,"=",result2[i],sep='')

pylab.plot(wyniki1,wyniki2)
pylab.show()

