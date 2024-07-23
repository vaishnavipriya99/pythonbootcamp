inp="helloworld"
ans=""
sum=0
for i in inp:
    if i not in ans:
        ans+=i
        sum+=1
print("sum of ans",sum)

    