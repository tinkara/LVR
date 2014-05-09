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
	
'''
sprejme slovar resitve in sestavi resen sudoku
'''
def Sudoku_solution_print(sol):
	#print sol
	if sol=="Ni resitve.":
		return sol
	else:
		sudoku=[[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None],
    	[None,None,None,None,None,None,None,None,None]]
		for i in range(9):
			for j in range(9):
				for k in range(9):
					var="i"+str(i)+"j"+str(j)+"k"+str(k)
					if sol[var]==True:
						if sudoku[i][j]==None:
							sudoku[i][j]=k+1
						else:
							print "napacna resitev!"
		return sudoku
           
'''
Sprejme nerešen sudoku in ga izriše in reši ter izriše dobljeno rešitev.
Če rešitve ni izpiše "Ni rešitve"
Če ugotovimo, da je rešitev napačna (primer v polju (1,1) imamo rešitev 1 in 5), potem vrne "napacna resitev!"
'''	
def Sudoku_solve(sudoku):
	print "input"
	print Sudoku_print(sudoku)
	sudoku_SAT = red.Sudoku(sudoku)
	#print sudoku_SAT
	sudoku_SAT_CNO=sudoku_SAT.cno()
	#print sudoku_SAT_CNO
	resitev= dpll.DPLL(sudoku_SAT_CNO)
	#print resitev
	resitev_print=Sudoku_solution_print(resitev)
	if resitev_print=="Ni resitve.":
		print "Ni resitve."
	else:
		print "output"
		print Sudoku_print(resitev_print)


'''PRIMERI'''		
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


'''TUKAJ vnesemo sudoku, ki ga zelimo resiti'''

print Sudoku_solve(sudoku2)






