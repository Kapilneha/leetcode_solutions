def remove_spaces(s):
    result = []

    for ch in s:
        if ch != ' ':
            result.append(ch)

    return ''.join(result)


s = input("Enter a string: ")
print(remove_spaces(s))