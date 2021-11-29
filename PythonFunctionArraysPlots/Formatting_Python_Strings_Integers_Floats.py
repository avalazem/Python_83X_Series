"""
    Name:     Mark
    Date:     January 14th, 2021
    Purpose:  Formatting Strings, Integers and Floats
    Versions: First and Last
    
"""

myStr="This is a string"
myFlt=34392.783
myInt=123456

fmt="String = {0:20} Float = {1:15.2f}  Integer = {2:20d}"

print(1,fmt.format(myStr,myFlt,myInt))

fmt="String = {0:20} Float = {1:15.2e}  Integer = {2:20d}"

print(2,fmt.format(myStr,myFlt,myInt))

fmt="String = {0:^20} Float = {1:<15.2e}  Integer = {2:20d}"

print(3,fmt.format(myStr,myFlt,myInt))

fmt="String = {0:*^20} Float = {1:$<15.2e}  Integer = {2:->20d}"

print(4,fmt.format(myStr,myFlt,myInt))

fmt="String = {0:*^20} Float = {1:$<15.2e}  Integer = {2:->20e}"

print(5,fmt.format(myStr,myFlt,myInt))

fmt="String = {0:*^20} Float = {1:$<15.2e}  Integer = {2:->20.2e}"

print(6,fmt.format(myStr,myFlt,myInt))
