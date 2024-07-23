my_list=list(map(int,input().split(",")))
n=len(my_list)
total_sum=((n+1)*(n+2))/2
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
print(total_sum-sum)