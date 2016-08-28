#  sudo pip3 install numpy

import numpy

print("input first array separated by spaces:")
a = input()
a = a.split()
print ("input second array separated by spaces")
b = input()
b = b.split()
# print(set(a) & set (b)) # second build-in method
# print(set(a).intersection(b)) # third build-in method
c = numpy.intersect1d(a,b)
print(c)
