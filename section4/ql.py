import math
pow=math.pow

x=eval(input())
if x<2:
    print(abs(x))
elif x<6:
    print(x**2+5)
else:
    print((x-2)**3)
