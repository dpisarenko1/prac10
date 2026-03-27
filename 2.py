def fibonaci(n):
    if n <= 0:
        return 0

    fib = []
    a, b = 1, 1

    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    print(*fib)
    return None

fibonaci(int(input()))