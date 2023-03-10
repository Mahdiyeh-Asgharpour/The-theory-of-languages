import re
#input
string=str(input())
#pattern 
#we can't say [1990-2023] so we decompose this to 4 number 
pattern=r"199\d|20\d\d"
#answer
answer=re.findall(pattern, string)

if(answer !=[]):

    print(False)
else:
    print(True)
