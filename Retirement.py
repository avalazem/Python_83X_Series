"""
Created on Tues Oct 27 10:44:59 2020

@author: Dr. Mark E. Lehr

Purpose:  To illustrate a Retirement Scenario
"""

from SavingsAndRetirementFunctionLibrary import retire1

def main():
    
    #Initialize variables for the savings/retirement function
    #tests defined above
    PERCENT=100      #Conversion percent = 100
    presVal=0        #Present Value in Savings of $0
    salary=100000    #Salary in $'s
    
    for intRat in range(4,10,1):             #Interest Rate in %
        for depsit in range(10,25,5):        #Deposit in % of Salary
            for numCmpd in range(10,75,1):   #Number of periods in Years
                intRate=intRat/PERCENT
                deposit=salary*depsit/PERCENT
                if salary/intRate < retire1(presVal,intRate,numCmpd,deposit):
                    print("Int Rate= ","{:.2f}".format(intRate*PERCENT),"%",end="")
                    print("  Deposit = ",deposit/salary*PERCENT,"%",end="")
                    print("  Years = ",numCmpd)
                    break
            print()
        print()
    
main()