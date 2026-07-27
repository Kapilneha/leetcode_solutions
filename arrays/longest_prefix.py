def longestCommonPrefix(strs):

    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


strs = input("Enter words separated by space: ").split()

print(longestCommonPrefix(strs))