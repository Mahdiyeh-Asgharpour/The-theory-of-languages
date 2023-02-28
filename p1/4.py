import re
#input
string=str(input())
#pattern
#the special time doesn't have number in the left place in this minute 
pattern=r":[0-9]{1}0"
#answer
answer=re.findall(pattern, string)
if(answer==[]):
    print(False)
else:
    print(True)