###################################################################
# VAJA 2  - prevod problemov na SAT
#
# naloga 1 - barvanje grafov
# naloga 2 - sudoku
####################################################################

#!/usr/bin/python
# -*- coding: utf-8 -*-

bool = __import__ ('01_boolove_formule')

# Zdruzljivost za Python 2 in Python 3
try:
    basestring
except NameError:
    basestring = str

# BARVANJE GRAFA
# parameter graf: vhodni graf, je dan kot seznam povezav
# parameter c: je stevilo barv, s katerimi zelimo pobarvati graf
def barvanje_grafa(graf, c):
    if len(graf)==0:
        return False
    if len(graf)==1:
        if graf[0][0]==graf[0][1] and c==1:
            return True
        elif graf[0][0]==graf[0][1] and c!=1:
            return False
        elif c==1:
            return False
    elif c<=1:
        return False
    formula=bool.AND([])

    # vozlisca pobarvana z vsaj eno barvo - And1 in Or1
    # vozlisca pobarvana z najvec eno barvo - And2, And22 in Not2
    pregledani=[]
    And1 = bool.AND([])
    And2 = bool.AND([])
    for e in graf:
        for i in e:
            if i not in pregledani:
                pregledani.append(i)
                Or1 = bool.OR([])
                And22 = bool.AND([])
                for k in range(c):
                    C_ik = "C"+i+str(k+1)
                    var_k = bool.Var(C_ik)
                    Or1.seznam.append(var_k)
                    l=k+1
                    while l<c:
                        C_il = "C"+i+str(l+1)
                        var_l = bool.Var(C_il)
                        Not2 = bool.NOT(bool.AND([var_k, var_l]))
                        And22.seznam.append(Not2)
                        l += 1
                And1.seznam.append(Or1)
                And2.seznam.append(And22)
    formula.seznam.append(And1)
    formula.seznam.append(And2)
                    
    # dve povezani vozlisci nista iste barve - And3, And32 in Not3
    And3 = bool.AND([])
    for e in graf:
        And32 = bool.AND([])
        i = e[0]
        j = e[1]
        for k in range(c):
            C_ik = "C"+i+str(k+1)
            C_jk = "C"+j+str(k+1)
            var_ik = bool.Var(C_ik)
            var_jk = bool.Var(C_jk)
            And32.seznam.append(bool.NOT(bool.AND([var_ik,var_jk])))
        And3.seznam.append(And32)
    formula.seznam.append(And3)
    return formula

#Sudoku
def Sudoku(sud):
	n=9
	#preverimo, da smo dobili sudoku pravilne dimenzije
	assert len(sud)==n ,"Sudoku ni prave dimenzije"
	for i in range(n):
		assert len(sud[i])==n, "Sudoku ni prave dimenzije"
	
	#sestavili bomo seznam formul, ki morajo veljati
	seznam=[]
	
	for i in range(n):
		for j in range(n):
			
			#za polja, ki se nimajo prednastavljene barve
			#zagotoviti moramo, da je v polju natanko 1 stevilka
			if sud[i][j] == None:
				for k in range(n):
					Or=bool.OR([])
					var=bool.Var("i"+str(i)+"j"+str(j)+"k"+str(k))
					Or.seznam.append(bool.NOT(var))
					And=bool.AND([])
					for l in range(n):
						#nasa spremenljivka je x_ijk, ki jo tu predstavimo z i_j_k_, kjer so v _ vrednosti od 1-9 in predstavljajo
						#(i,j) koordinata v sudoku, k stevilo v polju
						var=bool.Var("i"+str(i)+"j"+str(j)+"k"+str(l))
						if k==l:
							And.seznam.append(var)
						else:
							And.seznam.append(bool.NOT(var))
						#And.seznam.append(var if k==l else bool.NOT(var))
					Or.seznam.append(And)
					seznam.append(Or)
				Or=bool.OR([])
				for k in range(n):
					var=bool.Var("i"+str(i)+"j"+str(j)+"k"+str(k))
					Or.seznam.append(var)
				seznam.append(Or)	
			#za prednastavljena polja negiramo tiste barve, ki niso k (k je dolocen)
			else:
				col=sud[i][j]
				for k_1 in range(n):
					var=bool.Var("i"+str(i)+"j"+str(j)+"k"+str(k_1))
					temp=k_1+1
					if str(col)==str(temp):
						seznam.append(var)
					else:
						seznam.append(bool.NOT(var))
					'''
					#vrstica
					var1=bool.Var("i"+str(i)+"j"+str(k_1)+"k"+str(col-1))
					if(j!=k_1):
						seznam.append(bool.NOT(var1))
					#stolpec
					var2=bool.Var("i"+str(k_1)+"j"+str(j)+"k"+str(col-1))
					if(i!=k_1):
						seznam.append(bool.NOT(var2))
						
			#v vsakem stolpcu morajo biti natanko stevila od 1 do 9
			Or=bool.OR([])
			dodaj=1
			for k in range(n):
				if str(sud[k][j]==str(i+1)):
					dodaj=0
				Or.seznam.append(bool.Var("i"+str(k)+"j"+str(j)+"k"+str(i)))
			if dodaj==1:
				seznam.append(Or)
			
			#v vsaki vrstici morajo biti natanko stevila od 1 do 9
			Or=bool.OR([])
			dodaj=1
			for k in range(n):
				if str(sud[j][k]==str(i+1)):
					dodaj=0
				Or.seznam.append(bool.Var("i"+str(j)+"j"+str(k)+"k"+str(i)))
			if dodaj==1:
				seznam.append(Or)
			'''
	#seznam.append("zacetek")
	#vsaka vrstica mora vsebovati natanko stevila od 1 do 9
	#vsaka barva
	for i in range(n):
		#za vsako spr
		for s1 in range(n):
			for s2 in range(n):
				Or_vrst=bool.OR([])
				Or_stolp=bool.OR([])
				varAnd=bool.Var("i"+str(s1)+"j"+str(s2)+"k"+str(i))
				Or_vrst.seznam.append(bool.NOT(varAnd))
				Or_stolp.seznam.append(bool.NOT(varAnd))
				And_vrst=bool.AND([])
				And_stolp=bool.AND([])
				for j in range(n):
					#stolpec
					if(s2==j):
						And_stolp.seznam.append(bool.Var("i"+str(s1)+"j"+str(j)+"k"+str(i)))
					else:
						And_stolp.seznam.append(bool.NOT(bool.Var("i"+str(s1)+"j"+str(j)+"k"+str(i))))
					#vrstica
					if(s1==j):
						And_vrst.seznam.append(bool.Var("i"+str(j)+"j"+str(s2)+"k"+str(i)))
					else:
						And_vrst.seznam.append(bool.NOT(bool.Var("i"+str(j)+"j"+str(s2)+"k"+str(i))))
				Or_vrst.seznam.append(And_vrst)
				Or_stolp.seznam.append(And_stolp)
				seznam.append(Or_vrst)
				seznam.append(Or_stolp)
	#seznam.append("konec")
						
	#vsak 3x3 podkvadrat mora vsebovati natanko stevila od 1 do 9
	#vsaka barva
	for i in range(n):
		#kvadrant
		for j in range(3):
			for k in range(3):
				#za vsako spr
				for s1 in range (3):
					for s2 in range (3):
						OrSpr=bool.OR([])
						varAnd=bool.Var("i"+str(3*j+s1)+"j"+str(3*k+s2)+"k"+str(i))
						OrSpr.seznam.append(bool.NOT(varAnd))
						And_3x3=bool.AND([])
						
						for l in range(3):
							for m in range(3):
								if str(sud[3*j+m][3*k+l]==str(i+1)):
									if ((3*j+m)==(3*j+s1) and (3*k+l)==(3*k+s2)):
										And_3x3.seznam.append(bool.Var("i"+str(3*j+m)+"j"+str(3*k+l)+"k"+str(i)))
									else:
										And_3x3.seznam.append(bool.NOT(bool.Var("i"+str(3*j+m)+"j"+str(3*k+l)+"k"+str(i))))
						OrSpr.seznam.append(And_3x3)
						seznam.append(OrSpr)
	return bool.AND(seznam)
	
sudo = \
[[None, '8',  None, '1',  '6',  None, None, None, '7' ],
 ['1',  None, '7',  '4',  None, '3',  '6',  None, None],
 ['3',  None, None, '5',  None, None, '4', '2',   None],
 [None, '9',  None, None, '3',  '2',  '7',  None, '4' ],
 [None, None, None, None, None, None, None, None, None],
 ['2',  None, '4',  '8',  '1',  None, None, '6',  None],
 [None, '4',  '1', None,  None, '8',  None, None, '6' ],
 [None, None, '6', '7',   None, '1', '9',   None, '3' ],
 ['7',  None, None, None, '9',  '6',  None, '4',  None]]

sudo2= \
[[None,'2','3'],['2','3','1'],['3','1','2']]

#sudoku_formula = Sudoku(sudo2)
##
#print sudoku_formula.__repr__()


