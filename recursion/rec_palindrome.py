def rec_palindrome(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return rec_palindrome(s[1:-1])
    return False
