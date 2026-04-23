n = int(input("Enter value of n: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, n):
        if num % i == 0:
            return False
    return True
f = [fibonacci(i) for i in range(n+1)]
result = [x for x in f if is_prime(x) and x % 5 != 0]
print(result)