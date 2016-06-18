#-------------------------------------------------
#
# Project created by QtCreator 2016-04-29T23:04:45
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = KnapsackProblem
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    knapsackwindow.cpp \
    cipherwndow.cpp \
    decipherwindow.cpp \
    item.cpp \
    selection.cpp

HEADERS  += mainwindow.h \
    cipher.h \
    decipher.h \
    knapsackwindow.h \
    cipherwndow.h \
    decipherwindow.h \
    item.h \
    selection.h

FORMS    += mainwindow.ui \
    knapsackwindow.ui \
    cipherwndow.ui \
    decipherwindow.ui
