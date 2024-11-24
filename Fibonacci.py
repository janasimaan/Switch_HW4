def fibonacci_seq(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)


n = 6
result = fibonacci_seq(n)
print(result)

