a=int(input())
x=int(a**0.5)+1
count=0
if a==1:
    print("not a prime")
elif a==2:
    print("prime")
else:
    for i in range(2,x):
        if(a%i==0):
            count=1
            break
        if(count==0):
            print("a is prime")
        else:
            print("a is not a prime")
