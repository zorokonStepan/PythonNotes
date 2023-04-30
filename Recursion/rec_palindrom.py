def palindrom(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return palindrom(s[1:-1])
    return False


print(palindrom('шалаш'))
print(palindrom('йцйй'))