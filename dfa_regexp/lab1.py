# coding=utf-8


# 2-е задание: Построить программу конечного распознавателя для заданного языка:
# за каждым вхождением пары "11" следует "0";
# 3-е задание: Построить КА для распознавания цепочек и анализа ошибок, которые:
# состоят из арифметических выражений и не содержат скобок;


def fsm(stt, word):
    cond = stt[0]
    state = stt[1]
    for one in range(len(word)):
        check = False
        for two in range(1, len(state) - 1):
            for three in cond[two]:
                if word[one] == three:
                    if isinstance(state[two], int):
                        check = True
                        state = stt[state[two]]
                        if one == len(word) - 1:
                            if not state[len(state) - 1]:
                                print "Last terminal isn't finite!"
                                return -1
                            else:
                                print "The word fits."
                                return 0
                        break
                    elif isinstance(state[two], str):
                        print "Invalid word/expression!"
                        print state[two]
                        return -2
                    else:
                        print "Unexpected error!"
                        return -3
            if check:
                break
        if not check:
            print "Word has a symbol not from nonterminals alphabet!"
            return -4


def gramright(stt):
    alf = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cond = stt[0]
    for one in range(1, len(stt)):
        state = stt[one]
        rule = alf[one] + " ::= "
        for two in range(1, len(state) - 1):
            mpt = stt[state[two]][len(state) - 1]
            endl = two != len(state) - 2
            rule += cond[two]
            rule += alf[state[two]]
            if endl or mpt:
                rule += " | "
            if mpt:
                rule += cond[two]
                if endl:
                    rule += " | "
        print rule


def gramleft(stt):
    alf = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cond = stt[0]
    rule = []
    for i in range(1, len(stt)):
        rule.append(alf[i] + " ::= ")
    for one in range(1, len(stt)):
        state = stt[one]
        for two in range(1, len(state) - 1):
            rule[state[two] - 1] += alf[one]
            rule[state[two] - 1] += cond[two]
            rule[state[two] - 1] += " | "
            if one == 1:
                rule[state[two] - 1] += cond[two]
                rule[state[two] - 1] += " | "
    for i in range(len(rule)):
        res = list(rule[i])
        res[len(res) - 2] = " "
        del res[-3:]
        print "".join(res)


# Задание 1:
example = [
    [None, '0', '1', None],
    [1, 1, 2, True],
    [2, 3, 4, False],
    [3, 2, 1, True],
    [4, 1, 2, False]
]
gramright(example)
print
gramleft(example)

# Задание 2:
print
t2stt = [
    [None, '0', '1', None],
    [1, 1, 2, True],
    [2, 1, 3, True],
    [3, 1, "After every pair '11' should stand '0'.", False]
]
w = input("Enter a word: ")
fsm(t2stt, w)

# Задание 3:
print
t3stt = [
    [None, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "0", "123456789", "-", "+*/", None],
    [1, 2, "First digit of a number can't be zero.", 4, 3, "Expression can't start with a sign except minus.", False],
    [2, 2, 2, 2, 5, 5, False],
    [3, 2, "First digit of a number can't be zero.", 4, "Two or more signs can't stand together.",
     "Two or more signs can't stand together.", False],
    [4, "Letters can't stand between or after digits.", 4, 4, 5, 5, False],
    [5, 6, "First digit of a number can't be zero.", 7, "Two or more signs can't stand together.",
     "Two or more signs can't stand together.", False],
    [6, 6, 6, 6, 5, 5, True],
    [7, "Letters can't stand between or after digits.", 7, 7, 5, 5, True]
]
w = input("Enter a word: ")
fsm(t3stt, w)
