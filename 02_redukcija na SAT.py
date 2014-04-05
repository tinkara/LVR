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



#Sudoku
def Sudoku(sud):
	
	#preverimo, da smo dobili sudoku pravilne dimenzije
	assert len(sud)==9 ,"Sudoku ni prave dimenzije"
	for i in range(9):
		assert len(sud[i])==9, "Sudoku ni prave dimenzije"
	
	#sestavili bomo seznam formul, ki morajo veljati
	seznam=[]
	
	
	for i in range(9):
		for j in range(9):
			
			#za polja, ki se nimajo prednastavljene barve
			#zagotoviti moramo, da je v polju natanko 1 stevilka
			if sud[i][j] == None:
				Or=bool.OR([])
				for k in range(9):
					And=bool.AND([])
					for l in range(9):
						#nasa spremenljivka je x_ijk, ki jo tu predstavimo z i_j_k_, kjer so v _ vrednosti od 1-9 in predstavljajo
						#(i,j) koordinata v sudoku, k stevilo v polju
						var=bool.Var("i"+str(i+1)+"j"+str(j+1)+"k"+str(k+1))	
						And.seznam.append(var if k==l else bool.NOT(var))
					Or.seznam.append(And)
				seznam.append(Or)
			#za prednastavljena polja negiramo tiste barve, ki niso k (k je dolocen)
			else:
				col=sud[i][j]
				for k_1 in range(9):
					var=bool.Var("i"+str(i+1)+"j"+str(j+1)+"k"+str(k_1+1))
					seznam.append(var if col==k_1+1 else bool.NOT(var))
			
			#v vsakem stolpcu morajo biti natanko stevila od 1 do 9
			Or=bool.OR([])
			for k in range(9):
				Or.seznam.append(bool.Var("i"+str(k+1)+"j"+str(j+1)+"k"+str(i+1)))
			seznam.append(Or)
			
			#v vsaki vrstici morajo biti natanko stevila od 1 do 9
			Or=bool.OR([])
			for k in range(9):
				Or.seznam.append(bool.Var("i"+str(j+1)+"j"+str(k+1)+"k"+str(i+1)))
			seznam.append(Or)
		
		#vsak 3x3 podkvadrat mora vsebovati natanko stevila od 1 do 9
		for j in range(3):
			for k in range(3):
				Or=bool.OR([])
				for l in range(3):
					for m in range(3):
						Or.seznam.append(bool.Var("i"+str(3*j+m+1)+"j"+str(3*k+l+1)+"k"+str(i+1)))
				seznam.append(Or)
	return bool.AND(seznam)
	
sudo = \
[[None, '8', None, '1', '6', None, None, None, '7'],
 ['1', None, '7', '4', None, '3', '6', None, None],
 ['3', None, None, '5', None, None, '4', '2', None],
 [None, '9', None, None, '3', '2', '7', None, '4'],
 [None, None, None, None, None, None, None, None, None],
 ['2', None, '4', '8', '1', None, None, '6', None],
 [None, '4', '1', None, None, '8', None, None, '6'],
 [None, None, '6', '7', None, '1', '9', None, '3'],
 ['7', None, None, None, '9', '6', None, '4', None]]

sudoku_formula = Sudoku(sudo)

print sudoku_formula.__repr__()
