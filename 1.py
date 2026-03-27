def f(line):
    cnt_vowel = 0
    cnt_consonant = 0

    for char in line:
        if char in 'уеыаоэяиюё':
            cnt_vowel += 1

        if char in 'бвгджзйклмнпрстфхчцшщ':
            cnt_consonant += 1

    print(cnt_vowel)
    print(cnt_consonant)

f(input())