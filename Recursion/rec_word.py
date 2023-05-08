def sim(s):
    if 0 < len(s) < 3:
        return s
    return s[0] + '(' + sim(s[1:-1]) + ')' + s[-1]


if __name__ == "__main__":
    assert sim('aaaagxrdfuyihoilhgyrdtxdcfujvhkjbln;kkjhhxzdsxdjbk ghjlk/laaaa') == 'a(a(a(a(g(x(r(d(f(u(y(i(h(o(i(' \
                                                                                    'l(h(g(y(r(d(t(x(d(c(f(u(j(v(h(k' \
                                                                                    'j)b)l)n);)k)k)j)h)h)x)z)d)s)x)d)' \
                                                                                    'j)b)k) )g)h)j)l)k)/)l)a)a)a)a'
