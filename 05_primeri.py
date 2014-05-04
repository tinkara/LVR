#!/usr/bin/python
# -*- coding: utf-8 -*-

# Zdruzljivost za Python 2 in Python 3 la
try:
    basestring
except NameError:
    basestring = str


#OSNOVE
'''
Ustvarjanje spremenljivk in uporaba operandov negacija, AND in OR.
Operaciji AND in OR sprejmeta seznam kot argument.
'''

#import paketa, kjer so razredi za delo z boolovimi formulami
bool = __import__ ('01_boolove_formule')

print "OSNOVE"
print

#konstanti true in false
print "konstanta true: ",bool.Tru()
print "konstanta false: ",bool.Fls()

#ustvarjanje spremenljivk
p = bool.Var('p')
q = bool.Var('q')
r = bool.Var('r')
print "Spremenljivke p, q in r so ustvarjene:", p, q,r

#negacija
p = bool.NOT(p)
print "Negarana spremenljivka p:", p

#AND
f_and = bool.AND([p,q])
print "Operand AND: ",f_and

#OR
f_or = bool.AND([p,q,r])
print "Operand OR: ",f_or

print
print "==================================================================="
print

#EVALUACIJA

print "EVALUACIJA"
print

'''
Klic metode evaluate().
'''

print "Evaluacia Tru:", bool.Tru().evaluate()
print "Evaluacija spremenljivke:", bool.Var(False)
p = bool.Var(True)
q = bool.Var(True)
r = bool.Var(False)
f_eval = bool.AND([p, bool.OR([q,r])])
print "Formule f =",f_eval," -> evaluacija ", f_eval.evaluate()

print
print "==================================================================="
print

#SIMPLIFY

print "SIMPLIFY"
print

print
print "==================================================================="
print

#REDUKCIJA NA SAT

#import paketa, kjer so metode za redukcijo problemov na SAT
red = __import__ ('02_redukcija_na_SAT')

print "REDUKCIJA NA SAT"
print

#BARVANJE GRAFA
'''
Graf je podan kot seznam povezav med tockami v grafu.
'''

print "1. Barvanje grafa"
print
cikel = [['a','b'],['b','c'],['c','d'],['d','e'],['e','a']]
c1 = 3
cikel_sat = red.barvanje_grafa(cikel, c1)
print "cikel:", cikel
print
print "cikel SAT:", cikel_sat
print

poln_graf = [['a','b'],['a','c'],['a','d'],['a','e'],['b','c'],['b','d'],['b','e'],['c','d'],['c','e'],['d','e']]
c2 = 4
poln_graf_sat = red.barvanje_grafa(poln_graf, c1)
print "poln graf:", poln_graf
print
print "poln graf SAT:", poln_graf_sat
print

#SUDOKU
print "2. Sudoku"
print

print
print "==================================================================="
print

#PRETVORBA V CNO

print
print "==================================================================="
print

#DPLL

#import paketa, kjer se nahaja DPLL
dpll = __import__ ('03_DPLL')

print "DPLL"
print

'''
Formula mora biti podana v CNO. Ce temu ni tako,
jo je potrebno predhodno pretvoriti.

Kot resitev dobimo slovar spremenljivk in njihove vrednosti.
Ce se spremenljivka ne nahaja v slovarju, je lahko kar koli (ali True
ali False). Glej primer 2.
Ce je formula neresljiva, se izpise "Ni resitve.". Glej primer 3.
'''

p = bool.Var('p')
q = bool.Var('q')
r = bool.Var('r')

f1=bool.AND([bool.OR([q,r]), bool.OR([r,bool.NOT(p)]),p])
res1 = dpll.DPLL(f1)
print "Formula 1:", f1
print "Resitev 1:", res1
print

f2=bool.AND([p, bool.OR([r,p,q])])
res2 = dpll.DPLL(f2)
print "Formula 2:", f2
print "Resitev 2:", res2
print

f3=bool.AND([p,q, bool.OR([bool.NOT(p),bool.NOT(q)])])
res3 = dpll.DPLL(f3)
print "Formula 3:", f3
print "Resitev 3:", res3
print







