"""
    Name:     Mark
    Date:     September  23th, 2021
    Purpose:  Truth Table for Relational Operators
    Versions: First and Last
    
"""

#Output the Heading for Relational Table
fmtHdng="{0:^10}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}{7:^10}"
print(fmtHdng.format('a','b','a==b','a!=b','a<b','a<=b','a>b',"a>=b"))

#First Row of the Table
a=4
b=3
print(fmtHdng.format(a,b,a==b,a!=b,a<b,a<=b,a>b,a>=b))

#Second Row of the Table
a=4
b=4
print(fmtHdng.format(a,b,a==b,a!=b,a<b,a<=b,a>b,a>=b))

#Third Row of the Table
a=4
b=5
print(fmtHdng.format(a,b,a==b,a!=b,a<b,a<=b,a>b,a>=b))

#Now recreate the table with not 0,1 but with True/False
print()
print(fmtHdng.format('a','b','a==b','a!=b','a<b','a<=b','a>b',"a>=b"))
fmtCell='{0:^10}'
#First Row of the Table
a=4
b=3
print(fmtCell.format(a),end="")
print(fmtCell.format(b),end="")
cellVal="True" if a==b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a!=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>=b else "False"
print(fmtCell.format(cellVal))

#Second Row of the Table
a=4
b=4
print(fmtCell.format(a),end="")
print(fmtCell.format(b),end="")
cellVal="True" if a==b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a!=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>=b else "False"
print(fmtCell.format(cellVal))

#Third Row of the Table
a=4
b=5
print(fmtCell.format(a),end="")
print(fmtCell.format(b),end="")
cellVal="True" if a==b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a!=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a<=b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>b else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if a>=b else "False"
print(fmtCell.format(cellVal))