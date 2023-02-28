import re
#input
string=str(input())
#pattern
#if you see chocolate say false
pattern=r"chocolate"
#answer
answer=re.findall(pattern, string)
if(answer!=[]):
    print(False)
else:
    print(True)