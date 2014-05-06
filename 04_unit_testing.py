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
        G2 = [['a','b']]
        #na eni barvi
        c=1
        self.assertEqual(dpll.DPLL(red.barvanje_grafa(G2, c)), False)
        #na dveh barvah
        c=2
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G2,c)).cno()), {'Ca1': True,'Ca2': False,'Cb1': False, 'Cb2': True})
        #na petih barvah
        c=5
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G2,c)).cno()), {'Ca1': True, 'Ca2': False, 'Ca3': False, 'Ca4': False, 'Ca5': False, 'Cb2': True,'Cb1': False, 'Cb3': False, 'Cb4': False, 'Cb5': False})

        #poln graf na 4 tockah
        G4 = [['a','b'],['a','c'],['a','d'],['b','c'],['b','d'],['c','d']]
        #na treh barvah
        c=3
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G4,c)).cno()), "Ni resitve.")
        #na stirih barvah
        c=4
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G4,c)).cno()),{'Ca1': True, 'Cb2': True, 'Cc3': True, 'Cd4': True, 'Cd2': False, 'Ca3': False, 'Ca2': False, 'Cd3': False, 'Cc1': False, 'Ca4': False, 'Cb3': False, 'Cb1': False, 'Cd1': False, 'Cb4': False, 'Cc4': False, 'Cc2': False})

        #cikel na 7 tockah
        G7 = [['a','b'],['b','c'],['c','d'],['d','e'],['e','f'],['f','g'],['g','a']]
        #na dveh barvah
        c=2
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G7,c)).cno()), "Ni resitve.")
        #na treh barvah
        c=3
        self.assertEqual(dpll.DPLL((red.barvanje_grafa(G7,c)).cno()), {'Cg2': False, 'Ce1': True, 'Ca3': False, 'Ca2': False, 'Ca1': True, 'Cc1': True, 'Cc3': False, 'Cc2': False, 'Cb2': True, 'Cb3': False, 'Cb1': False, 'Ce3': False, 'Cd1': False, 'Cd2': True, 'Cd3': False, 'Cg1': False, 'Cg3': True, 'Cf1': False, 'Cf2': True, 'Cf3': False, 'Ce2': False})
        
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
	'''def test_same_vars(self):
		"testiranje OR in AND z isto spremenljivko"
		a=bool.Var("a")
		p= bool.OR([a,a])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
		p=bool.AND([a,a])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
	def test_true_false_var(self):
		"testiranje OR in AND, ko je ena spremenljivka true ali false"
		a=bool.Var("a")
		p=bool.OR([a,bool.Fls()])
		tr=bool.Tru()
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
		p=bool.OR([a,bool.Tru()])
		self.assertEqual(str(bool.Tru()),str(p.simplify()), "napacna poenostavitev, pricakovano true")
		p=bool.AND([a,bool.Fls()])
		self.assertEqual(str(bool.Fls()),str(p.simplify()), "napacna poenostavitev, pricakovano false")
		p=bool.AND([a,bool.Tru()])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
	def test_p_not_p(self):
		a=bool.Var("a")
		p=bool.AND([a,bool.NOT(a)])
		self.assertEqual(str(bool.Fls()),str(p.simplify()), "napacna poenostavitev, pricakovano false")
		p=bool.OR([a,bool.NOT(a)])
		self.assertEqual(str(bool.Tru()),str(p.simplify()), "napacna poenostavitev, pricakovano true")
	def test_complecs(self):
		a=bool.Var("p")
		b=bool.Var("q")
		c=bool.Var("r")
		# NOT p AND NOT q = NOT (p OR q)
		p=bool.AND([bool.NOT(a),bool.NOT(b)])
		t=bool.NOT(bool.OR([a,b]))
		self.assertEqual(str(t),str(p.simplify()), "napacna poenostavitev, pricakovano NOT (p OR q)")
		# NOT p OR NOT q = NOT (p AND q)
		p=bool.OR([bool.NOT(a),bool.NOT(b)])
		t=bool.NOT(bool.AND([a,b]))
		self.assertEqual(str(t),str(p.simplify()), "napacna poenostavitev, pricakovano NOT (p AND q)")
		
		# p AND (p OR q) = p
		p=bool.AND([a,bool.OR([a,b])])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano p")
		# (p OR r) AND (q OR r) = (p AND q) OR r
		p=bool.AND([bool.OR([a,b]), bool.OR([c,b])])
		t=bool.OR([bool.AND([a,c]), b])
		self.assertEqual(str(t),str(p.simplify()), "napacna poenostavitev, pricakovano (p AND q) OR r")
		#p OR (p AND q) = p
		p=bool.OR([a,bool.AND([a,b])])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano p")
		#(p AND r) OR (q AND r) = (p OR q) AND r
		p=bool.OR([bool.AND([a,b]), bool.AND([c,b])])
		t=bool.AND([bool.OR([a,c]), b])
		self.assertEqual(str(t),str(p.simplify()), "napacna poenostavitev, pricakovano (p OR q) AND r")'''

class DPLL_test(unittest.TestCase):
    def test_dpll(self):
        p = bool.Var('p')
        q = bool.Var('q')
        r = bool.Var('r')
        s = bool.Var('s')
        t = bool.Var('t')
        #konstanti
        self.assertEqual(dpll.DPLL(bool.Tru()), True)
        self.assertEqual(dpll.DPLL(bool.Fls()), False)
        #spremenljivka in negacija
        self.assertEqual(dpll.DPLL(p), {'p':True})
        self.assertEqual(dpll.DPLL(bool.NOT(p)), {'p':False})
        #prazen AND
        f1 = bool.AND([])
        self.assertEqual(dpll.DPLL(f1), "Ni resitve.")
        #AND z eno spr
        f2 = bool.AND([p])
        self.assertEqual(dpll.DPLL(f2), {'p':True})
        #AND z enim NOT
        f3 = bool.AND([bool.NOT(p)])
        self.assertEqual(dpll.DPLL(f3), {'p':False})
        # p A NOT p
        f4 = bool.AND([p, bool.NOT(p)])
        self.assertEqual(dpll.DPLL(f4), "Ni resitve.")
        # p A q A (NOT p V NOT q)
        f5 = bool.AND([p, q, bool.OR([bool.NOT(p), bool.NOT(q)])])
        self.assertEqual(dpll.DPLL(f5), "Ni resitve.")
        #sami literali
        f6 = bool.AND([p,q,r,s,bool.NOT(t)])
        self.assertEqual(dpll.DPLL(f6), {'q': True, 'p': True, 's': True, 'r': True, 't': False})
        # brez literalov - (p V q) A (NOT p V NOT q)
        f7 = bool.AND([bool.OR([p,q]), bool.OR([bool.NOT(p), bool.NOT(q)])])
        self.assertEqual(dpll.DPLL(f7), {'p':True, 'q':False})

if __name__ == '__main__':
    unittest.main()
