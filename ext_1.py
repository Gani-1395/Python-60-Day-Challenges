n = int(input("Enter the number of entries: "))
b = int(input("Enter the divisor: "))
if b == 0:
    print("Divisor cannot be zero!")
else:
    a = [x / b for x in range(n) if x.is_integer()]
    print(a)
