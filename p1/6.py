import re
#input
string=str(input())
#pattern
#it doesn't have letterings from g to z because it's begin from 0 to 15 
#from 0 to 9 is number but 10 is "A" 11 is"B" etc
#you count ,you understand 15 is "F" so in this we don't have G and another lettering
pattern=r"[G-Z]"
#answer
answer=re.findall(pattern, string)

if(answer!=[] ):
    print(False)
else:
    print(True)