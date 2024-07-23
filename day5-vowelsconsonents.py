vowels="aeiou"
consonents="bcdfghjklmnpqstvwxyz"
ans=""
inp="helloworld"
for i in inp:
    if i in vowels:
        ans+=i
print(ans)
for i in inp:
    if i in consonents:
        ans+=i
print(ans)

