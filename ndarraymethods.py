import numpy as np

a = np.arange(5)
print "a = ",a
print "Clipped", a.clip(1, 2) #所有比给定最大值还大的元素设定为给定的最大值，最小值亦然

a = np.arange(4)
print a
print "Compressed", a.compress(a > 2)#返回一个根据给定条件筛选后的数组

b = np.arange(1,9)
print "b = ",b
print "Factorial", b.prod()#所有元素的乘积

print "Factorials",b.cumprod()#所有元素的累积乘积
