vowels="aeiou"
consonents="bcdfghjklmnpqstvwxyz"
ans=""
inp="helloworld"
for i in inp:
    if i not in ans:
        ans+=i
print(ans)