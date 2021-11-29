"""
Purpose: Read a file then output first word
"""

#First word of each line
def first_word_of_each_line(fileName):
    lst=[]
    fileStuff = open(fileName,'r')
    lines=fileStuff.readlines()
    for line in lines:
        word=line.split()
        if len(word)>0:
            lst.append(word[0])
    return lst

file="JanWeek3AssignmentProblem3textfile.py"
print(first_word_of_each_line(file))