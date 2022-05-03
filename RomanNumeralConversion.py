# -*- coding: utf-8 -*-
"""
/* 
 * Author: Dr. Mark E. Lehr
 * Purpose:  Roman Numeral Conversion
 */
 """

#Function to convert Arabice numbers to Roman Numerals
def cArbcRm(arabic):
    #Declare all Variables Here
    #Input or initialize values Here
    #Process/Calculations Here
    romnNm=""
    n1000s=int(arabic/1000)  #/Determine # 1000'S
    arabic-=n1000s*1000      #Subtract from the Original Arabic
    n100s=int(arabic/100)    #Repeat process for all digits
    arabic-=n100s*100        #Repeat process for all digits
    n10s = arabic//10        #Repeat process for all digits
    arabic-=n10s*10          #Repeat process for all digits
    n1s =   arabic           #Repeat process for all digits
    
    #Output the #1000's in Roman Numerals
    if(n1000s==3): romnNm+="MMM"
    if(n1000s==2): romnNm+="MM"
    if(n1000s==1): romnNm+="M"
    

    #Output the #100's in Roman Numerals
    if(n100s==9): romnNm+="CM";
    if(n100s==8): romnNm+="DCCC";
    if(n100s==7): romnNm+="DCC";
    if(n100s==6): romnNm+="DC";
    if(n100s==5): romnNm+="D";
    if(n100s==4): romnNm+="CD";
    if(n100s==3): romnNm+="CCC";
    if(n100s==2): romnNm+="CC";
    if(n100s==1): romnNm+="C";
    
    #Output the #10's in Roman Numerals
    if  (n10s==9): romnNm+="XC"
    elif(n10s==8): romnNm+="LXXX"
    elif(n10s==7): romnNm+="LXX"
    elif(n10s==6): romnNm+="LX"
    elif(n10s==5): romnNm+="L"
    elif(n10s==4): romnNm+="XL"
    elif(n10s==3): romnNm+="XXX"
    elif(n10s==2): romnNm+="XX"
    elif(n10s==1): romnNm+="X"
        
    #Output the #10's in Roman Numerals
    romnNm+="IX"   if n1s==9 else \
            "VIII" if n1s==8 else \
            "VII"  if n1s==7 else \
            "VI"   if n1s==6 else \
            "V"    if n1s==5 else \
            "IV"   if n1s==4 else \
            "III"  if n1s==3 else \
            "II"   if n1s==2 else \
            "I"    if n1s==1 else ""

    return romnNm
    
#Test the Function Out
#Input or initialize values Here
arabic=int(input("Roman Numeral Conversion Input Arabic Year i.e. 0 to 3000\n"))
    
#Process/Calculations Here
print(arabic,"=",cArbcRm(arabic))
