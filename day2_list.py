my_list=[1,2,3,4]
my_list.append(9999)
my_list.insert(8000,900)
print(len(my_list))

my_list.pop(2)
my_list_2=[5,6,7,8]
new_lst=my_list+my_list_2
new_lst=my_list.copy()
new_lst.pop()
print(*new_lst)
print(*my_list)

cnt=my_list.count(2)
print(cnt)
my_list.sort()
print(*my_list)