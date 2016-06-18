# coding=utf-8


capacity = 150


class Cargo:
    def __init__(self, p, c):
        self.weight = p
        self.value = c
        self.specific = float(c)/float(p)
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


def dec_cap(n):
    global capacity
    assert isinstance(n, int)
    capacity -= n


def sortbyspec(elem):
    assert isinstance(elem, Cargo)
    return elem.specific


def packing(l):
    global capacity
    assert isinstance(l, list)
    for one in l:
        assert isinstance(one, Cargo)
        if one.getweight() <= capacity:
            one.setpacked()
            dec_cap(one.getweight())


def printpacked(l):
    assert isinstance(l, list)
    for one in l:
        assert isinstance(one, Cargo)
        one.printcargo()


def gready_unittest():
    load = [Cargo(20, 5), Cargo(1, 1), Cargo(6, 2), Cargo(40, 10), Cargo(30, 7), Cargo(200, 50), Cargo(100, 5),
            Cargo(70, 12)]
    load.sort(key=sortbyspec, reverse=True)
    packing(load)
    printpacked(load)

gready_unittest()
