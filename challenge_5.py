n = input("enter your favourite number: ")
if n.isdigit():
    m = int(input())
    data = [0] * m
    for i in range(m):
        data[i] = int(input())
else:
    print("invalid number")
