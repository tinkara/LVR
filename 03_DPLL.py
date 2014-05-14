###################################################################
# VAJA 3  - implementacija SAT
#
# naloga 1 - pretorba izraz v CNO
# naloga 2 - DPLL
# naloga 3 - izboljsave DPLL
###################################################################

#!/usr/bin/python
# -*- coding: utf-8 -*-

bool = __import__ ('01_boolove_formule')

# Zdruzljivost za Python 2 in Python 3
try:
    basestring
except NameError:
    basestring = str

#Meoda, ki je implementacija DPLL algoritma.
#f je logicni izraz v CNO
#restore je kopija formule f
def DPLL_alg(f, restore):
	literali = {}
	ostalo = []
	boTrue = False
	for i in f.seznam:
		if i==False: return False
		elif i==True: pass
		elif isinstance(i, bool.Var):
			if str(i) in literali:
				if literali[str(i)]==False:
					return [False,{}]
			else:
				literali[str(i)] = True
		elif isinstance(i, bool.NOT):
			if str(i.vrednost) in literali:
				if literali[str(i.vrednost)]==True:
					return [False,{}]
			else:
				literali[str(i.vrednost)] = False
		else:
			count = 0
			for j in i.seznam:
				if isinstance(j, bool.Var):
					if str(j) not in literali and str(j) not in ostalo:
						ostalo.append(str(j))
				if isinstance(j, bool.NOT):
					if str(j.vrednost) not in literali and str(j.vrednost) not in ostalo:
						ostalo.append(str(j.vrednost))
					elif str(j.vrednost) in literali:
						if literali[str(j.vrednost)]==True:
							count += 1
			#ce imamo same NOT in je vse v literalih -> ni resitve
			if count==len(i.seznam): 
				return [False,{}]  
	temp = f.replace(literali)
	simpl = temp.simplify_dpll()
	if simpl==True: return [True, literali]
	if simpl.simplify_dpll()==True: return [True, literali]
	else: return DPLL_BF(f,restore, ostalo, literali)

#Metoda DPLL algortima, ki izvaja brute force iskanje resitev
#f je formula
#copy je kopija formule f
#ostalo je seznam spremenljivk, za katere ne poznamo vrednosti
#spr je slovar spremenljivk in njihovih vrednosti
def DPLL_BF(f,copy, ostalo, spr):
	if f==True: return [True, spr]
	elif f==False: return [False, spr]
	if len(ostalo)>0:
		#probamo s True
		name = str(ostalo[0])
		spr[name] = True
		del ostalo[0]
		temp = f.replace(spr)
		simpl = temp.simplify_dpll()
		result = DPLL_BF(simpl, copy, ostalo, spr)
		if result[0]==True: return result
		else:
			#vrnemo v prejsnje stanje in probamo s False
			spr[name] = False
			f = restore(copy)
			temp = f.replace(spr)
			simpl = temp.simplify_dpll()
			result = DPLL_BF(simpl,copy, ostalo, spr)
	#vrnemo koncno resitev
	f = restore(copy)
	temp = f.replace(spr)
	simpl = temp.simplify_dpll()
	if simpl==False:
		return [False, {}]
	return [True, spr]
    
    
#Pomozna metoda, ki ustvari kopijo formule.
def copy(f):
    and_list = []
    for i in f.seznam:
        or_list = []
        if (isinstance(i, bool.Var) or isinstance(i, bool.NOT) or i==True or i==False):
            and_list.append(i)
        else:
            for j in i.seznam:
                new_var=""
                if isinstance(j, bool.Var):
                    name = "copy_"+str(j.ime)
                    new_var = bool.Var(name)
                else:
                    name = "copy_"+str(j.vrednost)
                    new_var = bool.NOT(bool.Var(name))
                or_list.append(new_var)
            bool_or = bool.OR(or_list)
            and_list.append(bool_or)
    copy = bool.AND(and_list)
    return copy

#Pomozna metoda, ki iz kopije ustvari zacetno formulo.
def restore(copy):
    and_list = []
    for i in copy.seznam:
        or_list = []
        if (isinstance(i, bool.Var) or isinstance(i, bool.NOT) or i==True or i==False):
            and_list.append(i)
        else: 
            for j in i.seznam:
                new_var=""
                if isinstance(j, bool.Var):
                    name = str(j.ime)[5:]
                    new_var = bool.Var(name)
                else:
                    name = str(j.vrednost)[5:]
                    new_var = bool.NOT(bool.Var(name))
                or_list.append(new_var)
            bool_or = bool.OR(or_list)
            and_list.append(bool_or)
    f = bool.AND(and_list)
    return f


#Metoda, ki sortira formulo ter nato klice dpll algoritem, kjer dobimo resitev.
#Argument je formula f v CNO.
def DPLL_sort(f):
    f_sorted = []
    count = 0
    for i in f.seznam:
        if isinstance(i, bool.Var) or isinstance(i, bool.NOT):
            f_sorted.insert(0,i)
            count +=1
        else:
            pos = len(f_sorted)
            if pos>0 and pos>count:
                while len(i.seznam)<len(f_sorted[pos-1].seznam) and pos>count:
                    pos -= 1
            if pos==len(f_sorted):
                f_sorted.append(i)
            else:
                f_sorted.insert(pos,i)
    f_cno_sorted = bool.AND(f_sorted)
    restore = copy(f_cno_sorted)
    #print f_cno_sorted
    return DPLL_alg(f_cno_sorted,restore)

#Metoda, ki pozene klic sortiranja (tam pa se pozene algoritem).
#Argument je formula f v CNO.
def DPLL(f):
    if isinstance(f, bool.Var):
        return {str(f.ime): True}
    elif isinstance(f, bool.NOT):
        return {str(f.vrednost): False}
    elif isinstance(f, bool.Tru) or f==True:
        return True
    elif isinstance(f, bool.Fls) or f==False:
        return False
    elif len(f.seznam)==0:
        return "Ni resitve."
    elif len(f.seznam)==1:
        return DPLL(f.seznam[0])
    else:
        res = DPLL_sort(f)
        if res[0]==False:
            return "Ni resitve."
        else:
            return res[1]
            
