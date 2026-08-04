def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


words = input("enter:").split()


print(longest_common_prefix(words))