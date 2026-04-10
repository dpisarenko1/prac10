def common_multiplies(A, B, N):
    """
    finding common quotients of two numbers
    :param A: first number
    :param B: second number
    :param N: limit of quotient
    :return: common quotients
    """
    result = []

    if A > N or B > N:
        return None
    else:
        for i in range(1, N):
            if i % A == 0 and i % B == 0:
                result.append(i)

    return result

print(*common_multiplies(4,6, 50))
