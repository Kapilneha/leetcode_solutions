def to_uppercase(s):
    result = []

    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        else:
            result.append(ch)

    return ''.join(result)


s = input("Enter a string: ")
print(to_uppercase(s))