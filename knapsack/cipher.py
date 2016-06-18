# coding=utf-8

import random


def fir(y):
    def sec(x, z):
        return x * z != 0

    def thi(x, z=y):
        return z % x

    return y * reduce(sec, map(thi, range(2, int(pow(y, 0.5) + 1))), 1)


def chs(n, m):
    return random.choice(filter(None, map(fir, range(n, m))))


def superincreasing(number, first):
    t = [first]
    for it in range(1, number):
        t.append(sum(t) + random.randint(1, 9))
    return t


# wsi = superincreasing(8, 2)
# ssi = sum(wsi)
# qssi = chs(ssi + 1, ssi * 2)
# rssi = random.randint(1, qssi - 1)


def gen_open_key(w, r, q):
    assert isinstance(w, list)
    beta = []
    for elem in w:
        beta.append(elem * r % q)
    return beta

abc = "abcdefghijklmnopqrstuvwxyz "

abcbin = ["01100001", "01100010", "01100011", "01100100", "01100101", "01100110", "01100111", "01101000", "01101001",
          "01101010", "01101011", "01101100", "01101101", "01101110", "01101111", "01110000", "01110001", "01110010",
          "01110011", "01110100", "01110101", "01110110", "01110111", "01111000", "01111001", "01111010", "00100000"]

abcbinhashmap = {}
binabchashmap = {}

for one in range(len(abc)):
    abcbinhashmap[abc[one]] = abcbin[one]

for one in range(len(abc)):
    binabchashmap[abcbin[one]] = abc[one]


def convert(string):
    global abcbinhashmap
    assert isinstance(string, str)
    string = string.lower()
    temp = []
    for symbol in string:
        temp.append(abcbinhashmap[symbol])
    return temp


def ciphering(key, conv):
    assert isinstance(key, list)
    assert isinstance(conv, list)

    s = 0
    sl = []

    for i in range(len(conv)):
        for j in range(len(conv[i])):
            s += int(conv[i][j]) * key[j]
        sl.append(s)
        s = 0
    return sl


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def knapsack(w, x):
    assert isinstance(w, list)
    assert isinstance(x, int)

    s = []
    m = x
    wtemp = list(reversed(w))
    for num in range(len(wtemp)):
        mtemp = filter(lambda n: n <= m, wtemp)
        if mtemp and wtemp[num] == max(mtemp) and m > 0:
            s.append('1')
            m = m - wtemp[num]
        else:
            s.append('0')
    s.reverse()
    return ''.join(s)


def deconvert(string):
    global binabchashmap
    assert isinstance(string, str)
    return binabchashmap[string]


def deciphering(cipher, w, r, q):
    global binabchashmap
    assert isinstance(cipher, list)

    s = []
    rs = []
    rrs = []
    mr = modinv(r, q)

    for c in cipher:
        s.append(c * mr % q)
    for x in s:
        rs.append(knapsack(w, x))
    for f in rs:
        rrs.append(deconvert(f))

    return ''.join(rrs)


def unittest(wtest, rtest, qtest):
    print wtest
    print rtest
    print qtest
    ktest = gen_open_key(wtest, rtest, qtest)
    print ktest
    ctest = convert(input("Input string to cipher: "))
    print ctest
    cip = ciphering(ktest, ctest)
    print cip
    res = deciphering(cip, wtest, rtest, qtest)
    print res

wsi = [2, 3, 9, 23, 42, 86, 174, 346]
rssi = 113
qssi = 971

unittest(wsi, rssi, qssi)
