m=int(input())
data=[0]*m
num_lst=[""]*m
str_lst=[" "]*m
n_count=0
s_count=0
for i in range(m):
    data[i]=(input())
for i in range(m):
    if data[i].isdigit():
        num_lst[n_count] = int(data[i])
        n_count += 1
    elif data[i] != '""':
        str_lst[s_count] = data[i]
        s_count += 1
num_lst = num_lst[:n_count]
str_lst = str_lst[:s_count]
reg_no = input("enter the registration number:")
if int(reg_no[-1]) % 2 == 0:
    num_lst = num_lst[::-1]
else:
    str_lst = str_lst[::-1]
print("Numbers List:", num_lst)
print("String List:", str_lst)
print("Total Numbers:", n_count)
print("Total Strings:", s_count)





