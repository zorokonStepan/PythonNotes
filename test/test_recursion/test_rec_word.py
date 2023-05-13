from recursion.rec_word import rec_word


def test_rec_word():
    assert rec_word('aaaagxrdfuyihoilhgyrdtxdcfujvhkjbln;kkjhhxzdsxdjbk ghjlk/laaaa') == \
           'a(a(a(a(g(x(r(d(f(u(y(i(h(o(i(l(h(g(y(r(d(t(x(d(c(f(u(j(v(h(kj)b)l)n);' \
           ')k)k)j)h)h)x)z)d)s)x)d)j)b)k) )g)h)j)l)k)/)l)a)a)a)a'
