import re
#input
input=str(input())
#pattern float
pattern=r"[+-]?[0-9]+\.[0-9]+"
#answer 
#i print answer and i understand if the number is not float answer=none 
answer=re.search(pattern,input)
if(answer==None):
    print(False)
else:
    print(True)