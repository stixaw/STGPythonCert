# Fibonacci number module


def fibonacci(num):
    result = 0
    if num <= 1:
        result = num
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    return result


def fib_loop(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fib(n):  # write Fibonacci series up to n
    a: int
    a, b = 0, 1
    while b < n:
        result = b,
        a, b = b, a + b
        print(result)


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def fib_looper(n):
    if n <= 1:
        result = n
        print(n)
    else:
        fib_list = [0, 1]
        i = 2
        while i < n + 1:
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
            i += 1
        for num in fib_list:
            print(num)
