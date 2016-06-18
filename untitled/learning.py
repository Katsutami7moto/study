# coding=utf-8


example = [
    [False, '0', '1', False],
    [1, 1, 2, True],
    [2, 3, 4, False],
    [3, 2, 1, True],
    [4, 1, 2, False]
]

ident = [
    [False, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
     "_", "0", "123456789", ".", "[", "]", False],
    [1, 2, 3, False, False, False, False, False, False],
    [2, 2, 2, 2, 2, 5, 4, False, True],
    [3, 2, 3, False, False, False, False, False, False],
    [4, 8, False, 7, 6, False, False, False, False],
    [5, 10, False, False, False, False, False, False, False],
    [6, False, False, 6, 6, False, False, 9, False],
    [7, False, False, False, False, False, False, 9, False],
    [8, 8, 8, 8, 8, False, False, 9, False],
    [9, False, False, False, False, 5, 4, False, True],
    [10, 10, 10, 10, 10, False, 4, False, True]
]


# def mysqrt(n):
#     i = n
#     while (i * i - n) > 0.000000001:
#         i = 0.5 * (i + n / i)
#         print "i ", i
#     print "Result ", i


def mysqrt(n):
    def s(a=n):
        if a * a - n > 0.000000001:
            s(0.5 * (a + n / a))
            print "a ", a
        else:
            print "Result ", a

    return s


# f = mysqrt(123456)
# f


def mypwr(x, n):
    if n < 0:
        return 1.0 / mypwr(x, -n)
    else:
        if n == 0:
            return 1
        else:
            if n % 2.0 == 0:
                return mypwr(x * x, n / 2)
            else:
                return x * mypwr(x * x, (n - 1) / 2)


def myroot(x, n):
    n = float(n)
    i = x
    while (mypwr(i, n) - x) > 0.000000001:
        i = ((n-1)*i + x/mypwr(i, n-1))/n
    return i

print myroot(151, 5)
print mypwr(2, 10)
print mypwr(myroot(151, 5), 5)


def sumofsquares(n):
    return sum(map(lambda x: x * x, range(1, n)))


# print sumofsquares(100)


def gcd(first, second):
    assert isinstance(first, int)
    assert isinstance(second, int)

    a, b = first, second

    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def coprime(first, second):
    assert isinstance(first, int)
    assert isinstance(second, int)

    if gcd(first, second) == 1:
        return True
    else:
        return False


def fib(n):
    if n >= 0:
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)


def fibl(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b


# print fibl(33333)

# print fib(20)
# mysqrt(fib(20))


def multab():
    m = int(raw_input("Введи число:"))
    a = int(raw_input("Введи число:"))
    b = int(raw_input("Введи число:"))
    for x in range(a, b + 1):
        print m, " * ", x, " = ", m * x

# multab()
