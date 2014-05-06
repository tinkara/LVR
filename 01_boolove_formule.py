###################################################################
# VAJA 1 - osnovne strukture in funkcije
#
# naloga 1 - podatkovna struktura za Boolove formule
# naloga 2 - funkcija/metoda, ki vrne vrednost Boolove formule
# naloga 3 - funkcija/metoda za poenostavljanje izrazov
###################################################################

#!/usr/bin/python

# -*- coding: utf-8 -*-

# Zdruzljivost za Python 2 in Python 3
try:
    basestring
except NameError:
    basestring = str

#razred za predstavitev konstante T
class Tru():
    def __init__(self):
        pass
    def __repr__(self):
        return "True"
    def evaluate(self):
        return True
    def replace(self,v):
        return True
    def flatten(self):
        return "True"
    def cno(self):
        return "True"
    def simplify(self):
    	return self
    def simplify_dpll(self):
        return True

#razred za predstavitev konstante F
class Fls():
    def __init__(self):
        pass
    def __repr__(self):
        return "False"
    def evaluate(self):
        return False
    def replace(self, v):
        return False
    def flatten(self):
        return "False"
    def cno(self):
        return "False"
    def simplify(self):
    	return self
    def simplify_dpll(self):
        return False

#razred za predstavitev AND
class AND:
    def __init__(self, seznam):
        self.seznam=seznam
    def __repr__(self):
        s=""
        k=1
        if len(self.seznam)==0:
            s = str(Fls())
            return s
        else:
            for i in self.seznam:
                if k == len(self.seznam):
                    s = s + str(i)
                else:
                    s = s + str(i) + ' A '
                k += 1
        return '(' + s + ')'
    def evaluate(self):
        for i in self.seznam:
            if i==False:
                return False
            elif isinstance(i,AND) or isinstance(i,OR) or isinstance(i,NOT) or isinstance(i,Var):
                if i.evaluate()==False:
                    return False
        return True
    def replace(self, dic):
        novi_seznam = []
        for i in self.seznam:
            if i==True:
                novi_seznam.append(True)
            elif i==False:
                novi_seznam.append(False)
            elif isinstance(i, Var):
                if str(i) in dic:
                    novi_seznam.append(i.replace(dic[str(i)]))
                else:
                    novi_seznam.append(i)
            elif isinstance(i, NOT):
                if str(i.vrednost) in dic:
                    novi_seznam.append(i.replace(dic[str(i.vrednost)]))
                else:
                    novi_seznam.append(i)
            elif isinstance(i, AND) or isinstance(i, OR):
                s = i.replace(dic)
                novi_seznam.append(s)
        self.seznam = novi_seznam
        return AND(self.seznam)
    def simplify_dpll(self):
        count = 0
        new_seznam = []
        for i in self.seznam:
            if i==True:
                new_seznam.append(True)
                count += 1
            elif i==False:
                return False
            elif isinstance(i, NOT):
                s = i.simplify_dpll()
                if s==False:
                    return False
                else:
                    new_seznam.append(s)
            else:
                if len(i.seznam)==1:
                    if i.seznam[0]==True:
                        new_seznam.append(True)
                        count += 1
                    elif i.seznam[0]==False:
                        return False
                    else:
                        s = i.seznam[0].simplify_dpll()
                        if s==False:
                            return False
                else:
                    s = i.simplify_dpll()
                    if s==False:
                        return False
                    if s==True:
                        new_seznam.append(True)
                        count += 1
                    else:
                        new_seznam.append(s)
        self.seznam=new_seznam
        if count==len(self.seznam):
            return True
        else:
            return AND(self.seznam)
    def simplify(self):
        prvi = self.seznam[0]
        drugi = self.seznam[1]
        # p AND p = p
        if prvi==drugi:
            return prvi
        # p AND T = p, T AND p = p
        elif isinstance(prvi, Tru):
            return drugi
        elif isinstance(drugi, Tru):
            return prvi
        # p AND F = F
        elif isinstance(prvi,Fls) or isinstance(drugi,Fls):
            return Fls()
        # p AND NOT p = F, NOT p AND p = F
        neg_ime=""
        temp="1"
        if isinstance(prvi, NOT):
            neg_ime=prvi.vrednost
            temp=drugi
        if isinstance (drugi,NOT):
            neg_ime=drugi.vrednost
            temp=prvi
        if neg_ime==temp:
        	return Fls()
        # NOT p AND NOT q = NOT (p OR q)
        if isinstance(prvi, NOT) and isinstance(drugi, NOT):
        	return NOT(OR([prvi.vrednost,drugi.vrednost]))
        # p AND (p OR q) = p, (p OR q) AND p = p
        if isinstance(drugi, OR) and (drugi.seznam[0]==prvi or drugi.seznam[1]==prvi):
        	return prvi
        elif isinstance(prvi, OR) and (prvi.seznam[0]==drugi or prvi.seznam[1]==drugi):
            return drugi
        # (p OR r) AND (q OR r) = (p AND q) OR r
        if isinstance (prvi, OR) and isinstance(drugi, OR):
        	if prvi.seznam[0]==drugi.seznam[0]:
        		return OR([AND([prvi.seznam[1],drugi.seznam[1]]),prvi.seznam[0]])
        	elif prvi.seznam[0]==drugi.seznam[1]:
        		return OR([AND([prvi.seznam[1],drugi.seznam[0]]),prvi.seznam[0]])
        	elif prvi.seznam[1]==drugi.seznam[0]:
        		return OR([AND([prvi.seznam[0],drugi.seznam[1]]),prvi.seznam[1]])
        	elif prvi.seznam[1]==drugi.seznam[1]:
        		return OR([AND([prvi.seznam[0],drugi.seznam[0]]),prvi.seznam[1]])
        return self
     
    def flatten(self):
    	if len(self.seznam)==1:
    		return self.seznam[0].flatten()
    	else:
    		sez=[]
    		b=[a.flatten() for a in self.seznam]
    		for c in b:
    			if isinstance(c,AND):
    				sez=sez+c.seznam
    			else:
    				sez.append(c)
    		for d in sez:
    			if isinstance(d,OR) and len(d.seznam)==0:
    				return Fls()
    			elif len(sez)==1:
    				return l[0]
    			else:
    				return AND(sez)
    			    
    def cno(self):
    	"prevedba na konjunktivno normalno obliko"
    	if len(self.seznam)==0:
    		return self.seznam[0].cno()
    	else:
    		func=[]
    		for i in self.seznam:
    			func.append(i.cno())
    		return AND(func).flatten()

#razred za predstavitev OR
class OR:
    def __init__(self, seznam):
        self.seznam=seznam
    def __repr__(self):
        s=""
        k=1
        if len(self.seznam)==0:
            s = str(Fls())
            return s
        else:
            for i in self.seznam:
                if k == len(self.seznam):
                    s = s + str(i)
                else:
                    s = s + str(i) + ' V '
                k += 1
        return '(' + s + ')'
    def evaluate(self):
        for i in self.seznam:
            if i==True:
                return True
            elif isinstance(i,AND) or isinstance(i,OR) or isinstance(i,NOT) or isinstance(i,Var):
                if i.evaluate()==True:
                    return True
        return False
    def replace(self, dic):
        novi_seznam = []
        for i in self.seznam:
            if isinstance(i, str):
                i = Var(i)
            if isinstance(i, Var):
                if str(i) in dic:
                    novi_seznam.append(i.replace(dic[str(i)]))
                else:
                    novi_seznam.append(i)
            elif isinstance(i, NOT):
                if str(i.vrednost) in dic:
                    novi_seznam.append(i.replace(dic[str(i.vrednost)]))
                else:
                    novi_seznam.append(i)
            elif isinstance(i, AND) or isinstance(i, OR):
                novi_seznam.append(i.replace(dic))
        self.seznam = novi_seznam
        return OR(self.seznam)
    def simplify_dpll(self):
        new_seznam=[]
        count = 0
        for i in self.seznam:
            if i==True:
                return True
            elif i==False:
                new_seznam.append(False)
                count += 1
            elif isinstance(i, str):
                i = Var(i)
            elif isinstance(i, NOT):
                if i.vrednost==True:
                    new_seznam.append(False)
                    count += 1
                elif i.vrednost==False:
                    return True
                else:
                    new_seznam.append(i.simplify_dpll())
            elif isinstance(i, Var):
                if i.ime==False:
                    new_seznam.append(False)
                    count += 1
                elif i.ime==True:
                    return True
                else:
                    new_seznam.append(i.simplify_dpll())
            else:
                new_seznam.append(i.simplify_dpll())
        self.seznam=new_seznam
        if count==len(self.seznam):
            return False
        return OR(self.seznam)
    def simplify(self):
        prvi = self.seznam[0]
        drugi = self.seznam[1]
        # p OR p = p
        if prvi==drugi:
            return prvi
        # p OR T = T, T OR p = T
        elif prvi==True or drugi==True:
            return True
        # p OR F = p
        elif isinstance(prvi,Fls):
            return drugi
        elif isinstance(drugi,Fls):
            return prvi
        # p OR NOT p = T, NOT p OR p = T
        neg_ime=""
        temp="1"
        if isinstance(prvi, NOT):
            neg_ime=prvi.vrednost
            temp=drugi
        if isinstance (drugi,NOT):
            neg_ime=drugi.vrednost
            temp=prvi
        if neg_ime==temp:
            return Tru()
        # NOT p OR NOT q = NOT (p AND q) - ne smemo zaradi DPLL
##        if isinstance(prvi, NOT) and isinstance(drugi, NOT):
##        	return NOT(AND([prvi.vrednost,drugi.vrednost]))
        # p OR (p AND q) = p, (p AND q) OR p = p
        if isinstance(drugi, AND) and (drugi.seznam[0]==prvi or drugi.seznam[1]==prvi):
        	return prvi
        elif isinstance(prvi, AND) and (prvi.seznam[0]==drugi or prvi.seznam[1]==drugi):
            return drugi
        # (p AND r) OR (q AND r) = (p OR q) AND r
        if isinstance (prvi, AND) and isinstance(drugi, AND):
        	if prvi.seznam[0]==drugi.seznam[0]:
        		return AND([OR([prvi.seznam[1],drugi.seznam[1]]),prvi.seznam[0]])
        	elif prvi.seznam[0]==drugi.seznam[1]:
        		return AND([OR([prvi.seznam[1],drugi.seznam[0]]),prvi.seznam[0]])
        	elif prvi.seznam[1]==drugi.seznam[0]:
        		return AND([OR([prvi.seznam[0],drugi.seznam[1]]),prvi.seznam[1]])
        	elif prvi.seznam[1]==drugi.seznam[1]:
        		return AND([OR([prvi.seznam[0],drugi.seznam[0]]),prvi.seznam[1]])
        return self
    def flatten(self):
    	if len(self.seznam)==1:
    		return self.seznam[0].flatten()
    	else:
    		sez=[]
    		b=[a.flatten() for a in self.seznam]
    		for c in b:
    			if isinstance(c,OR):
    				sez=sez+c.seznam
    			else:
    				sez.append(c)
    		for d in sez:
    			if isinstance(d,AND) and len(d.seznam)==0:
    				return Tru()
    			elif len(sez)==1:
    				return l[0]
    			else:
    				return OR(sez)
    def cno(self):
    	"konjunktivna normalna oblika"
    	if len(self.seznam)==0:
    		return self.seznam[0].cno()
    	else:
    		flat=[i.cno() for i in self.seznam]
    		yes=[i for i in self.seznam if isinstance(i,AND)]
    		no=[i for i in self.seznam if not isinstance(i,AND)]
    		if len(yes)==0:
    			return OR(no)
    		else:
    			"konjunkcija vec disjunktov"
    			konj=[]
    			for i in yes[0].seznam:
    				temp=no+[i]+yes[1:]
    				konj.append(OR(temp).cno())
    			return AND(konj).flatten()   
        
#razred za predstavitev NEG
class NOT():
    def __init__(self, vrednost):
        self.vrednost=vrednost
    def __repr__(self):
        return 'NOT ' + str(self.vrednost)
    def evaluate(self):
        i = self.vrednost
        if i==True:
            return False
        elif i==False:
            return True
        else:
            return False
    def replace(self, v):
        if v==True:
            return NOT(True)
        elif v==False:
            return NOT(False)
        else:
            self.vrednost = v
            return NOT(self.vrednost)
    def simplify_dpll(self):
        if self.vrednost==True:
            return False
        elif self.vrednost==False:
            return True
        else:
            return NOT(self.vrednost)
    def simplify(self):
    	if isinstance(self.vrednost, NOT):
    		return self.vrednost.vrednost.simplify()
    	elif isinstance(self.vrednost, AND):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return OR(nots).simplify()
    	elif isinstance(self.vrednost, OR):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return AND(nots).simplify()
    	else:
    		return self
    def flatten(self):
    	if isinstance(self.vrednost, NOT):
    		return self.vrednost.vrednost.flatten()
    	elif isinstance(self.vrednost, AND):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return OR(nots).flatten()
    	elif isinstance(self.vrednost, OR):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return AND(nots).flatten()
    	else:
    		return self
    def cno(self):
    	if isinstance(self.vrednost, NOT):
    		return self.vrednost.vrednost.cno()
    	elif isinstance(self.vrednost, AND):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return OR(nots).cno()
    	elif isinstance(self.vrednost, OR):
    		nots=[NOT(a) for a in self.vrednost.seznam]
    		return AND(nots).cno()
    	else:
    		return self            

#razred za predstavitev spremenljivke
class Var:
    def __init__(self, ime):
        self.ime=ime
    def __repr__(self):
        return str(self.ime)
    def __eq__(self, ime2):
        if self.ime==ime2:
            return True
        return False
    def __hash__(self):
        return id(self)
    def evaluate(self):
        i = self.ime
        if i==True:
            return True
        elif i==False:
            return False
        else:
            return False
    def replace(self, v):
        if v==True:
            return True
        elif v==False:
            return False
        else:
            self.ime = v
        return Var(self.ime)
    def simplify_dpll(self):
        if self.ime==True:
            return True
        elif self.ime==False:
            return False
        else:
            return self.ime
    def flatten(self):
    	return self
    def cno(self):
    	return self
    def simplify(self):
    	return self


#test izpisov
#testni primer za poenostavljanje
##p=Var("p")
##q=Var("q")
##r=Var("r")
##
##f2 = AND([p,Fls()])
##print "poenostavitev f2:"
##print f2
##print f2.simplify()

"""
TESTING CNO

q = Var("q")
p = Var("p")
r = Var("r")
s = Var("s")
test_CNO_formula_1 = AND([OR([q,p, r]), OR([NOT(p), NOT(r)]), OR([NOT(q)])])
test_CNO_formula_2 = AND([NOT(p), OR([p,NOT(q)]), OR([p,q,r])])
test_CNO_formula_3 = AND([OR([p,q,r]), OR([p,NOT(q),r])])
test_CNO_formula_4 = AND([p, OR([NOT(p), q]), OR([NOT(p), NOT(q), NOT(r)])])

test_CNO_formula_5=NOT(OR([p,q]))
test_CNO_formula_6=OR([AND([p,r]),q])
test_CNO_formula_7=NOT(NOT(p))
"ali je treba se znebiti tudi oklepajev?"
test_CNO_formula_8=AND([p,OR([q,AND([r,s])])])

print test_CNO_formula_5.cno()

p=AND([Var("a"), Var("b")])
print p.simplify()
"""
##a=Var("a")
##b=Var("b")
##p=AND([NOT(a),NOT(b)])
##p=OR([a,Fls()])
##p=OR([a,Tru()])
##print p.simplify()

