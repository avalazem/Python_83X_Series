
#Playing with strings
print("Playing with Strings")
str="0123456789012345678901234567890"
print(str)
print(str[::])
print(str[3:25])
print(str[3:25:1])
print(str[3:25:2])
print(str[25:3:-1])
print(str[25:3:-2])
print(str[::-1])

#Playing with lists
print("Playing with Lists")
xlist=["Mark","Mary","Jim"]
print(xlist)
print(xlist[::])
print(xlist[::-1])
rlist=xlist[::-1]
print(rlist)

#Generating random numbers.
print("Playing with Random Numbers")
import random as r
from datetime import datetime as d
r.seed(d.now())
print(r.randint(1,10))
print(r.randint(1,10))
print(r.randint(1,10))
print(r.randint(1,10))
print(r.randint(1,10))
print(r.randint(1,10))
print(r.randint(1,10))