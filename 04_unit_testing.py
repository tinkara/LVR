#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
bool = __import__ ('01_boolove_formule')

# Zdruzljivost za Python 2 in Python 3 la
try:
    basestring
except NameError:
    basestring = str

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
	def test_more_nots(self):
		"testiranje za liho število negacij"
		p=bool.NOT(bool.NOT(bool.NOT(bool.Var("a"))))
		t=bool.NOT(bool.Var("a"))
		self.assertEqual(t, p.simplify(), "napacna poenostavitev, pricakovano NOT a")
		"testiranje za sodo stevilo negacij"
		p=bool.NOT(bool.NOT(bool.NOT(bool.NOT(bool.Var("a")))))
		t=bool.Var("a")
		self.assertEqual(t, p.simplify(), "napacna poenostavitev, pricakovano a")
	def same_vars(self):
		"testiranje OR in AND z isto spremenljivko"
		a=bool.Var("a")
		p= bool.OR([a,a])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
		p=bool.AND([a,a])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
	def true_false_var(self):
		"testiranje OR in AND, ko je ena spremenljivka true ali false"
		a=bool.Var("a")
		p=bool.OR(a,bool.Fls())
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
		p=bool.OR(a,bool.Tru())
		self.assertEqual(bool.Tru(),p.simplify(), "napacna poenostavitev, pricakovano true")
		p=bool.AND(a,bool.Fls())
		self.assertEqual(bool.Fls(),p.simplify(), "napacna poenostavitev, pricakovano false")
		p=bool.AND(a,bool.Tru())
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano a")
	def p_not_p(self):
		a=bool.Var("a")
		p=bool.AND([a,bool.NOT(a)])
		self.assertEqual(bool.Fls(),p.simplify(), "napacna poenostavitev, pricakovano false")
		p=bool.OR([a,bool.NOT(a)])
		self.assertEqual(bool.Tru(),p.simplify(), "napacna poenostavitev, pricakovano true")
	def complecs(self):
		a=bool.Var("p")
		b=bool.Var("q")
		# NOT p AND NOT q = NOT (p OR q)
		p=bool.AND([bool.NOT(a),bool.NOT(b)])
		t=bool.NOT(bool.OR([a,b]))
		self.assertEqual(t,p.simplify(), "napacna poenostavitev, pricakovano NOT (p OR q)")
		# p AND (p OR q) = p
		p=bool.AND([a,bool.OR([a,b])])
		self.assertEqual(a,p.simplify(), "napacna poenostavitev, pricakovano p")
		
if __name__ == '__main__':
    unittest.main()