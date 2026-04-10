def fibonaci(n):
    """
    :param n: the last number
    :return: fibonacci series
    """
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
