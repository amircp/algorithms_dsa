"""
    Practicing recursion
"""

def get_fibonnaci_numbers(n):

    a = 0
    b = 1

    while a < n:
        print(a, end=" ")
        c = a+b
        a = b
        b = c

get_fibonnaci_numbers(1000)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\r\n")
print(fibonacci(8))