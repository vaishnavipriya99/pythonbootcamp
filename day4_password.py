pw=input()
x=len(pw)
if(('@'and'/') in pw and x==8 and " "not in pw):
    print("weak")
elif(('@'and'/') in pw and x>8 and x<12 and " "not in pw):
    print("medium")
elif(('@'and'/') in pw and x>12 and x<15 and " "not in pw):
    print("strong")
else:
    print("follow the conditions")
    
    