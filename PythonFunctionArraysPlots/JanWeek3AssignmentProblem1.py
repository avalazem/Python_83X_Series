"""
Purpose: Counting arguments of functions
"""

#Determine the number of arguments
def all_the_kwargs(**kwargs):
    return len(kwargs)

print(all_the_kwargs(x=1,y=2,z=3,w=4))
print(all_the_kwargs(x=1,y=2,z=3))
print(all_the_kwargs(x=1,y=2))
print(all_the_kwargs(x=1))
print(all_the_kwargs(x="one",y="two",z="Three",w="four"))
print(all_the_kwargs(x="one",y="two",z="Three"))
print(all_the_kwargs(x="one",y="two"))
print(all_the_kwargs(x="one"))