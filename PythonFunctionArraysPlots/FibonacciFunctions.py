"""
Purpose: Almost Fibonacci
"""

#Almost Fibonacci Function
def almost_fibonacci(n):
    lst=[]
    if n>=1:
        lst.append(0)
    if n>=2:
        lst.append(1)
    if n>=3:
        lst.append(1)
    if n>=4:
        for i in range(4,n+1):
            fib=lst[i-2]+lst[i-3]+lst[i-4]
            lst.append(fib)
    return lst

for n in range(1,11):
    print(almost_fibonacci(n))

n=10    
print("The sequence for just",n,"=",end="")
for n in almost_fibonacci(n):
    print("",n,end="")
        