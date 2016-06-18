# coding=utf-8

import time

capacity = 150
optimal = 0
optsel = None


class Cargo:
    def __init__(self, p, c):
        self.weight = p
        self.value = c
        self.packed = False

    def setpacked(self):
        self.packed = True

    def getweight(self):
        return self.weight

    def getvalue(self):
        return self.value

    def getpacked(self):
        return self.packed

    def printcargo(self):
        if self.getpacked():
            print "(Weight = " + str(self.getweight()) + "; Value = " + str(self.getvalue()) + ")\n"


class Selection:
    def __init__(self, number, w, v):
        self.select_number = set()
        self.select_number.add(number)
        self.sum_weight = w
        self.sum_value = v

    def add(self, number, w, v):
        self.select_number.add(number)
        self.sum_weight += w
        self.sum_value += v

    def getnumber(self):
        return self.select_number

    def getweight(self):
        return self.sum_weight

    def getvalue(self):
        return self.sum_value


def repsel(l, c):
    global capacity, optimal, optsel
    assert isinstance(l, list)
    assert isinstance(c, list)
    ltemp = []
    check = False
    for one in l:
        for two in range(0, len(c)):
            assert isinstance(one, Selection)
            if two not in one.getnumber():
                temp = c[two]
                stemp = one
                assert isinstance(temp, Cargo)
                if stemp.getweight() + temp.getweight() <= capacity:
                    stemp.add(two, temp.getweight(), temp.getvalue())
                    if stemp.getvalue() > optimal:
                        optimal = stemp.getvalue()
                        optsel = stemp.getnumber()
                        ltemp.append(stemp)
                    check = True
    if check:
        repsel(ltemp, c)


def selecting(cargoslist):
    global capacity
    assert isinstance(cargoslist, list)
    start = []
    check = False
    for i in range(0, len(cargoslist)):
        temp = cargoslist[i]
        assert isinstance(temp, Cargo)
        if temp.getweight() <= capacity:
            stemp = Selection(i, temp.getweight(), temp.getvalue())
            start.append(stemp)
            check = True
    if check:
        repsel(start, cargoslist)


def packing(l):
    global optsel
    assert isinstance(optsel, set)
    assert isinstance(l, list)
    for i in range(0, len(l)):
        if i in optsel:
            l[i].setpacked()


def printpacked(l):
    assert isinstance(l, list)
    for one in l:
        assert isinstance(one, Cargo)
        one.printcargo()


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)


def branch_unittest():
    load = [Cargo(20, 5), Cargo(1, 1), Cargo(6, 2), Cargo(40, 10), Cargo(30, 7), Cargo(200, 50), Cargo(100, 5),
            Cargo(70, 12)]
    with Profiler() as p:
        selecting(load)
    packing(load)
    print optsel
    printpacked(load)

branch_unittest()
