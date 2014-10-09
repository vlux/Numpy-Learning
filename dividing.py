import numpy as np
from __future__ import division

a = np.array([2,6,5])
b = np.array([1,2,3])

print "Divide",np.divide(a,b),np.divide(b,a)
print "True Divide",np.true_divide(a,b), np.true_divide(b,a) #不做截断直接返回
print "Floor Divide",np.floor_divide(a,b), np.floor_divide(b,a)    #等价于先调用divide再调用floor

c = 3.14 * b

print "Floor Divide 2",np.floor_divide(c,b), np.floor_divide(b,c)
print "/ operator", a/b, b/a
print "// operator", a//b, b//a
print "// operator 2", c//b, b//c
