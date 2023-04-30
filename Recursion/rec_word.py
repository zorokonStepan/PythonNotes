def sim(s):
    if 0 < len(s) < 3:
        return s
    return s[0] + '(' + sim(s[1:-1]) + ')' + s[-1]


print(sim('aaaagxrdfuyihoilhgyrdtxdcfujvhkjbln;kkjhhxzdsxdjbk ghjlk/laaaa'))
