###################################################################
# VAJA 2  - prevod problemov na SAT
#
# naloga 1 - barvanje grafov
# naloga 2 - sudoku
# naloga 3 - Hadamardova matrika
###################################################################

#!/usr/bin/python
# -*- coding: utf-8 -*-

bool = __import__ ('01_boolove_formule')

# Zdruzljivost za Python 2 in Python 3
try:
    basestring
except NameError:
    basestring = str

def barvanje_grafa():
    pass


#primer - cikel na 5 tockah, ali ga lahko pobarvamo s 3 barvami
V=["a","b","c","d","e"]
E=[["a","b"],["b","c"],["c","d"],["d","e"],["a","e"]]
k=3
