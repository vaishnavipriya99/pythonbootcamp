my_list=[1,2,3,4,6]
k=int(input())
n=int(input())
if(len<k+n):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n],end="")
        break

