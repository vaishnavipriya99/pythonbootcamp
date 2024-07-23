inp="XYZ"
char=''
n=0
for i in inp:
    n=ord(i)
    char+=chr(n-23)
print(char)
    