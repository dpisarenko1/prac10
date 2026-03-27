def length_limit(line):
    if len(line) <= 160:
        return line
    else:
        return line[:160]

print(length_limit('балалайка'))
