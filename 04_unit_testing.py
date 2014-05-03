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

if __name__ == '__main__':
    unittest.main()