# coding=utf-8


abc = "abcdefghijklmnopqrstuvwxyz "

abcbin = ['01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', '01101000', '01101001',
          '01101010', '01101011', '01101100', '01101101', '01101110', '01101111', '01110000', '01110001', '01110010',
          '01110011', '01110100', '01110101', '01110110', '01110111', '01111000', '01111001', '01111010', '00100000']

binabchashmap = {}

for one in range(len(abc)):
    binabchashmap[abcbin[one]] = abc[one]


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


cip = [393, 651, 643, 1050, 1247, 46, 893, 1755, 393, 1542]
wtest = [2, 3, 9, 23, 42, 86, 174, 346]
rtest = 113
qtest = 971

res = deciphering(cip, wtest, rtest, qtest)
print res
