import re
#input
string=str(input())
#pattern
#just the first lettering is captal the answer is false
pattern=r"function\s[A-Z]+()"
#answer
answer=re.findall(pattern, string)

if(answer!=[]):
    print(False)
else:
    print(True)