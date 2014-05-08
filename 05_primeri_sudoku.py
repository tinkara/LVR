#!/usr/bin/python
# -*- coding: utf-8 -*-

# Zdruzljivost za Python 2 in Python 3 la
try:
    basestring
except NameError:
    basestring = str
bool = __import__ ('01_boolove_formule')
red = __import__('02_redukcija_na_SAT')
dpll = __import__('03_DPLL')

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
	print Sudoku_print(sudoku)
	sudoku_SAT = red.Sudoku(sudoku)
	#print sudoku_SAT
	sudoku_SAT_CNO=sudoku_SAT.cno()
	#print sudoku_SAT_CNO
	resitev= dpll.DPLL(sudoku_SAT_CNO)
	print resitev
		
sudoku1 = [[None, 8, None, 1, 6, None, None, None, 7],
			[1, None, 7, 4, None, 3, 6, None, None],
			[3, None, None, 5, None, None, 4, 2, None],
			[None, 9, None, None, 3, 2, 7, None, 4],
			[None, None, None, None, None, None, None, None, None],
			[2, None, 4, 8, 1, None, None, 6, None],
			[None, 4, 1, None, None, 8, None, None, 6],
			[None, None, 6, 7, None, 1, 9, None, 3],
			[7, None, None, None, 9, 6, None, 4, None]]

sudoku2 = [[None,9,2,3,4,8,1,5,7],
           [7,4,3,5,6,1,9,8,2],
           [8,1,5,2,9,7,6,3,4],
           [5,8,6,1,2,3,7,4,9],
           [4,3,1,7,8,9,5,2,6],
           [2,7,9,6,5,4,8,1,3],
           [9,5,8,4,7,2,3,6,1],
           [1,2,7,8,3,6,4,9,5],
           [3,6,4,9,1,5,2,7,8]]
sudo2= \
[[None,'2','3'],['2','3','1'],['3','1','2']]


#print Sudoku_print(sudoku2)

#sudoku_SAT = red.Sudoku(sudo2)
#print sudoku_SAT

#sudoku_SAT_CNO = sudoku_SAT.cno()
#print sudoku_SAT_CNO

print Sudoku_solve(sudoku2)






