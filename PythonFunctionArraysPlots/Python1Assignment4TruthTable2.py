"""
    Name:     Mark
    Date:     September 23, 2021
    Purpose:  Truth Table for Logical Operators
    Versions: First and Last
    
"""

#Output the Heading for Logical Table
fmtHdng="{0:^10}{1:^10}{2:^10}{3:^10}{4:^10}{5:^10}"
print(fmtHdng.format('p','q','not p','not q','p or q','p and q'))

#First Row of the Table
p=True
q=True
print(fmtHdng.format(p,q,not p,not q,p or q,p and q))


#Second Row of the Table
p=True
q=False
print(fmtHdng.format(p,q,not p,not q,p or q,p and q))

#Third Row of the Table
p=False
q=True
print(fmtHdng.format(p,q,not p,not q,p or q,p and q))

#Fourth Row of the Table
p=False
q=False
print(fmtHdng.format(p,q,not p,not q,p or q,p and q))


#Now recreate the table with not 0,1 but with True/False
print()
print(fmtHdng.format('p','q','not p','not q','p or q','p and q'))

fmtCell='{0:^10}'
#First Row of the Table
p=True
q=True
cellVal="True" if p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p or q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p and q else "False"
print(fmtCell.format(cellVal))

#Second Row of the Table
p=True
q=False
cellVal="True" if p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p or q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p and q else "False"
print(fmtCell.format(cellVal))

#Third Row of the Table
p=False
q=True
cellVal="True" if p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p or q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p and q else "False"
print(fmtCell.format(cellVal))

#Fourth Row of the Table
p=False
q=False
cellVal="True" if p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not p else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if not q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p or q else "False"
print(fmtCell.format(cellVal),end="")
cellVal="True" if p and q else "False"
print(fmtCell.format(cellVal))