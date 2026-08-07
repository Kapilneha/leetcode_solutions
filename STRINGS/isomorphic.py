def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for i in range(len(s)):
        ch1 = s[i]
        ch2 = t[i]

        if ch1 in map_st and map_st[ch1] != ch2:
            return False

        if ch2 in map_ts and map_ts[ch2] != ch1:
            return False

        map_st[ch1] = ch2
        map_ts[ch2] = ch1

    return True


s = "egg"
t = "add"

print(is_isomorphic(s, t))