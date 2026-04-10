def length_limit(line):
    """
    checking for string length
    :param line: start line
    :return: string up to 160 characters
    """
    if len(line) <= 160:
        return line
    else:
        return line[:160]

print(length_limit('балалайка'))
