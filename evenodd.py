num=int(input())
if(num%2==0 and num<0):
    print("the number is  negative even")
elif(num%2==0 and num>0):
    print("the number is positive even")
elif(num%2!=0 and num<0):
    print("the number is negative odd")
else:
    print("the number is positive odd")