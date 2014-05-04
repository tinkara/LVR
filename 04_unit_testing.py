#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
bool = __import__ ('01_boolove_formule')
red = __import__('02_redukcija_na_SAT')
dpll = __import__('03_DPLL')

# Zdruzljivost za Python 2 in Python 3
try:
    basestring
except NameError:
    basestring = str

#Metoda za testiranje podatkovnih struktur in osnovnih funkcij
class bool_test(unittest.TestCase):
    def test_osnove(self):
        self.assertEqual(str(bool.Tru()), "True")
        self.assertEqual(str(bool.Fls()), "False")
        p = bool.Var("p")
        q = bool.Var("q")
        self.assertEqual(p, "p")
        self.assertEqual(str(bool.NOT(p)), "NOT p")
        self.assertEqual(str(bool.AND([p,q])), "(p A q)")
        self.assertEqual(str(bool.OR([p,q])),"(p V q)")
        #prazen seznam
        self.assertEqual(str(bool.AND([])), str(bool.Fls()))
        self.assertEqual(str(bool.OR([])), str(bool.Fls()))
    def test_evaluate(self):
        #konstanti
        self.assertEqual(bool.Tru().evaluate(), True)
        self.assertEqual(bool.Fls().evaluate(), False)
        #spremenljivka
        t=bool.Var(bool.Fls())
        self.assertEqual(t.evaluate(), False)
        #prazna formula
        f=bool.OR([])
        self.assertEqual(f.evaluate(), False)
        #sestavljena formula 1
        x=bool.Var("x")
        y=bool.Var("y")
        v = {x: False, y: True}
        f=bool.OR([bool.Tru(),bool.OR([v[y], bool.Fls()]),bool.AND([bool.NOT(bool.NOT(v[x])),v[y]]),bool.NOT(v[x])])
        self.assertEqual(f.evaluate(), True)
        #sestavljena formula 2
        p=bool.Var(False)
        q=bool.Var(True)
        r=bool.Var(True)
        f_primer = bool.AND([bool.OR([p,q]),bool.OR([p,r]),bool.OR([r,p]),bool.NOT(bool.AND([p,q])), bool.NOT(bool.AND([q,r])),bool.NOT(bool.AND([r,p]))])
        self.assertEqual(f_primer.evaluate(), False)

class red_test(unittest.TestCase):
    def test_barvanje_grafa(self):
        #graf brez povezav
        G = []
        self.assertEqual(red.barvanje_grafa(G,2), False)
        #graf na eni tocki (povezana sama s seboj)
        G1 = [['a','a']]
        self.assertEqual(red.barvanje_grafa(G1,1), True)
        self.assertEqual(red.barvanje_grafa(G1,2), False)

        #graf na dveh tockah
        #(tocka a pobarvana z barvo 1, tocka b pobarvana z barvo2)
##        G2 = [['a','b']]
##        print G2
##        c=2
##        G2_SAT = red.barvanje_grafa(G2, c)
##        print "G2 SAT"
##        print G2_SAT
##        print
##        G2_SAT_CNO = G2_SAT.cno()
##        print "G2_SAT_CNO"
##        print G2_SAT_CNO
##        print dpll.DPLL(G2_SAT_CNO)
##        self.assertEqual(dpll.DPLL(G2_SAT_CNO),{'Ca1': True, 'Ca2': False, 'Cb1': True, 'Cb2': False})

        ##        G2 = [['a','b'],['b','c'],['c','a']]
        

        
    def test_sudoku(self):
        pass

    


class Simplify_test(unittest.TestCase):
	"""Metoda za testiranje metode simplify"""
	def test_already_simplified(self):
		"testiranje ze poenostavljene formule, vrniti mora prvotno formulo"
		p=bool.Fls()
		self.assertEqual(p,p.simplify(), "Napacna poenostavitev, pricakovan Fls")
		
	def test_already_simplified2(self):
		"testiranje ze poenostavljene formule, vrniti mora prvotno formulo"
		p=bool.AND([bool.Var("a"), bool.Var("b")])
		self.assertEqual(p,p.simplify(),"Napacna poenostavitev, pricakovan a AND b") 
##	def test_more_nots(self):
##		"testiranje za liho število negacij"
##		p=bool.NOT(bool.NOT(bool.NOT(bool.Var("a"))))
##		t=bool.NOT(bool.Var("a"))
##		self.assertEqual(t, p.simplify(), "napacna poenostavitev, pricakovano NOT a")
##		"testiranje za sodo stevilo negacij"
##		p=bool.NOT(bool.NOT(bool.NOT(bool.NOT(bool.Var("a")))))
##		t=bool.Var("a")
##		self.assertEqual(t, p.simplify(), "napacna poenostavitev, pricakovano a")
##	def same_vars(self):
##		"testiranje OR in AND z isto spremenljivko"
##		a=bool.Var("a")
##		p= bool.OR([a,a])
##		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
##		p=bool.AND([a,a])
##		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
##	def true_false_var(self):
##		"testiranje OR in AND, ko je ena spremenljivka true ali false"
##		a=bool.Var("a")
##		p=bool.OR(a,bool.Fls())
##		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
##		p=bool.OR(a,bool.Tru())
##		self.assertEqual(bool.Tru(),p.simplify(), "napacna poenostavitev, pricakovano true")
##		p=bool.AND(a,bool.Fls())
##		self.assertEqual(bool.Fls(),p.simplify(), "napacna poenostavitev, pricakovano false")
##		p=bool.AND(a,bool.Tru())
##		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
##	def p_not_p(self):
##		a=bool.Var("a")
##		p=bool.AND([a,bool.NOT(a)])
##		self.assertEqual(bool.Fls(),p.simplify(), "napacna poenostavitev, pricakovano false")
##		p=bool.OR([a,bool.NOT(a)])
##		self.assertEqual(bool.Tru(),p.simplify(), "napacna poenostavitev, pricakovano true")
##	def complecs(self):
##		a=bool.Var("p")
##		b=bool.Var("q")
##		# NOT p AND NOT q = NOT (p OR q)
##		p=bool.AND([bool.NOT(a),bool.NOT(b)])
##		t=bool.NOT(bool.OR([a,b]))
##		self.assertEqual(t,p.simplify(), "napacna poenostavitev, pricakovano NOT (p OR q)")
##		# p AND (p OR q) = p
##		p=bool.AND([a,bool.OR([a5,b])])
##		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano p")

class DPLL_test(unittest.TestCase):
    def test_dpll(self):
        p = bool.Var('p')
        q = bool.Var('q')
        r = bool.Var('r')
        s = bool.Var('s')
        t = bool.Var('t')
##        #konstanti
##        self.assertEqual(dpll.DPLL(bool.Tru()), True)
##        self.assertEqual(dpll.DPLL(bool.Fls()), False)
##        #spremenljivka in negacija
##        self.assertEqual(dpll.DPLL(p), {'p':True})
##        self.assertEqual(dpll.DPLL(bool.NOT(p)), {'p':False})
##        #prazen AND
##        f1 = bool.AND([])
##        self.assertEqual(dpll.DPLL(f1), "Ni resitve.")
##        #AND z eno spr
##        f2 = bool.AND([p])
##        self.assertEqual(dpll.DPLL(f2), {'p':True})
##        f3 = bool.AND([bool.NOT(p)])
##        self.assertEqual(dpll.DPLL(f3), {'p':False})
##        # p A NOT p
##        f4 = bool.AND([p, bool.NOT(p)])
##        self.assertEqual(dpll.DPLL(f4), "Ni resitve.")
##        # p A q A (NOT p V NOT q)
##        f5 = bool.AND([p, q, bool.OR([bool.NOT(p), bool.NOT(q)])])
##        self.assertEqual(dpll.DPLL(f5), "Ni resitve.")
##        #sami literali
##        f6 = bool.AND([p,q,r,s,bool.NOT(t)])
##        self.assertEqual(dpll.DPLL(f6), {'q': True, 'p': True, 's': True, 'r': True, 't': False})
##        # brez literalov - (p V q) A (NOT p V NOT q)
##        f7 = bool.AND([bool.OR([p,q]), bool.OR([bool.NOT(p), bool.NOT(q)])])    
##        self.assertEqual(dpll.DPLL(f7), {'p':True, 'q':False})

if __name__ == '__main__':
    unittest.main()
