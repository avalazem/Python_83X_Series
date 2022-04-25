# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:57:55 2022

@author: mlehr
"""

strTab="{:^10}{:^10}{:^10}{:^10}"
print(strTab.format("a","b","a==b","a!=b"))
a=4
b=3
col3="True" if a==b else "False"
col4="True" if a!=b else "False"
print(strTab.format(a,b,col3,col4))
a=4
b=4
col3="True" if a==b else "False"
col4="True" if a!=b else "False"
print(strTab.format(a,b,col3,col4))
a=4
b=5
col3="True" if a==b else "False"
col4="True" if a!=b else "False"
print(strTab.format(a,b,col3,col4))
print()

strTab="{:^10}{:^10}{:^10}{:^10}{:^10}"
print(strTab.format("p","q","not p","p or q","p|q"))
p=True
q=True
col1="True" if p      else "False"
col2="True" if q      else "False"
col3="True" if not p  else "False"
col4="True" if p or q else "False"
col5="True" if p | q  else "False"
print(strTab.format(col1,col2,col3,col4,col5))
p=True
q=False
col1="True" if p      else "False"
col2="True" if q      else "False"
col3="True" if not p  else "False"
col4="True" if p or q else "False"
col5="True" if p | q  else "False"
print(strTab.format(col1,col2,col3,col4,col5))
p=False
q=True
col1="True" if p      else "False"
col2="True" if q      else "False"
col3="True" if not p  else "False"
col4="True" if p or q else "False"
col5="True" if p | q  else "False"
print(strTab.format(col1,col2,col3,col4,col5))
p=False
q=False
col1="True" if p      else "False"
col2="True" if q      else "False"
col3="True" if not p  else "False"
col4="True" if p or q else "False"
col5="True" if p | q  else "False"
print(strTab.format(col1,col2,col3,col4,col5))