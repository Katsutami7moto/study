# coding=utf-8


def dfareader(stt, word):
    state = 1
    assert isinstance(word, str)
    for symbol in word:
        if symbol in stt[state]:
            state = stt[state][symbol]
        else:
            print "Invalid word/expression!"
            return
    if stt[state][0]:
        print "The word fits."
        return
    else:
        print "Last terminal isn't finite!"
        return


# (ac|bc)*ad+
stti = {
    1: {'a': 3, 'b': 2, 0: False},
    2: {'c': 1, 0: False},
    3: {'c': 1, 'd': 4, 0: False},
    4: {'d': 4, 0: True}
}
w = input("Enter a word: ")
dfareader(stti, w)
