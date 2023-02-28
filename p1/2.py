import re
#input
string=str(input())
#pattern 
#we can't say [1990-2023] so we decompose this to 4 number 
pattern=r"[1-2]\d\d\d"
#answer
answer=re.findall(pattern, string)
if(int(answer[0])>=1990):
    print(False)
else:
    print(True)