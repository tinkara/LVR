#!/usr/bin/python
# -*- coding: utf-8 -*-

# Zdruzljivost za Python 2 in Python 3 la
try:
    basestring
except NameError:
    basestring = str
bool = __import__ ('01_boolove_formule')

'''lep izpis sudoka'''
def Sudoku_print(sudoku):
	out=""
	for i in range(len(sudoku)):
		if i%3==0 and i!=0:
			#out+="\n"
			out+="|-----------------------------|"
			out+="\n"
		for j in range(len(sudoku)):
			if j%3==0:
				out+="|"
			if sudoku[i][j]!=None:
				out+=" "+str(sudoku[i][j])+" "
			else:
				out+=" x "
		out+="|"
		out+="\n"
	return out
	
def Sudoku_solve(sudoku):
	pass
		
sudoku1 = [[None, 8, None, 1, 6, None, None, None, 7],
			[1, None, 7, 4, None, 3, 6, None, None],
			[3, None, None, 5, None, None, 4, 2, None],
			[None, 9, None, None, 3, 2, 7, None, 4],
			[None, None, None, None, None, None, None, None, None],
			[2, None, 4, 8, 1, None, None, 6, None],
			[None, 4, 1, None, None, 8, None, None, 6],
			[None, None, 6, 7, None, 1, 9, None, 3],
			[7, None, None, None, 9, 6, None, 4, None]]

print Sudoku_print(sudoku1)