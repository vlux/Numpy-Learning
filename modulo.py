import numpy as np

a = np.arange(-4, 4)

print "Remainder", np.remainder(a, 2)    #逐个返回两个数组中元素相除后的余数
print "Mod", np.mod(a, 2)
print "% operator",a % 2
print "Fmod", np.fmod(a, 2)    #所得余数的正负由被除数决定，与除数的正负无关
