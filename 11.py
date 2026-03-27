def prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

N = int(input())
result = []

for i in range(1, N + 1):
    if prime(i):
        result.append(i)

print(*result)