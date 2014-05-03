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
    def flatten(self):
        return "True"
    def cno(self):
        return "True"
    def simplify(self):
    	return self

#razred za predstavitev konstante F
class Fls():
    def __init__(self):
        pass
    def __repr__(self):
        return "False"
    def flatten(self):
        return "False"
    def cno(self):
        return "False"
    def simplify(self):
    	return self

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
        k=1
        for i in self.seznam:
            if i is not False and i is not True:
                i = i.evaluate()
            if i is False:
                return False
            k+=1
        return True
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
        	return NOT(OR(prvi,drugi))
        # p AND (p OR q) = p, (p OR q) AND p = p
        if isinstance(drugi, OR) and (drugi.seznam[0]==prvi or drugi.seznam[1]==prvi):
        	return prvi
        elif isinstance(prvi, OR) and (prvi.seznam[0]==drugi or prvi.seznam[1]==drugi):
            return drugi
        # (p OR r) AND (q OR r) = (p AND q) OR r
        if isinstance (prvi, OR) and isinstance(drugi, OR):
        	if prvi.seznam[0]==drugi.seznam[0]:
        		return OR(AND(prvi.seznam[1],drugi.seznam[1]),prvi.seznam[0])
        	elif prvi.seznam[0]==drugi.seznam[1]:
        		return OR(AND(prvi.seznam[1],drugi.seznam[0]),prvi.seznam[0])
        	elif prvi.seznam[1]==drugi.seznam[0]:
        		return OR(AND(prvi.seznam[0],drugi.seznam[1]),prvi.seznam[1])
        	elif prvi.seznam[1]==drugi.seznam[1]:
        		return OR(AND(prvi.seznam[0],drugi.seznam[0]),prvi.seznam[1])
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
            if i is not False and i is not True:
                i = i.evaluate()
            if i is True:
                return True
        return False
    def simplify(self):
        prvi = self.seznam[0]
        drugi = self.seznam[1]
        # p OR p = p
        if prvi==drugi:
            return prvi
        # p OR T = T, T OR p = T
        elif isinstance(prvi, Tru) or isinstance(drugi, Tru):
            return Tru()
        # p OR F = p
        elif isinstance(prvi,Fls):
        	return prvi
        elif isinstance(drugi,Fls):
            return drugi
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
        # NOT p OR NOT q = NOT (p AND q)
        if isinstance(prvi, NOT) and isinstance(drugi, NOT):
        	return NOT(AND(prvi,drugi))
        # p OR (p AND q) = p, (p AND q) OR p = p
        if isinstance(drugi, AND) and (drugi.seznam[0]==prvi or drugi.seznam[1]==prvi):
        	return prvi
        elif isinstance(prvi, AND) and (prvi.seznam[0]==drugi or prvi.seznam[1]==drugi):
            return drugi
        # (p AND r) OR (q AND r) = (p OR q) AND r
        if isinstance (prvi, OR) and isinstance(drugi, OR):
        	if prvi.seznam[0]==drugi.seznam[0]:
        		return AND(OR(prvi.seznam[1],drugi.seznam[1]),prvi.seznam[0])
        	elif prvi.seznam[0]==drugi.seznam[1]:
        		return AND(OR(prvi.seznam[1],drugi.seznam[0]),prvi.seznam[0])
        	elif prvi.seznam[1]==drugi.seznam[0]:
        		return AND(OR(prvi.seznam[0],drugi.seznam[1]),prvi.seznam[1])
        	elif prvi.seznam[1]==drugi.seznam[1]:
        		return AND(OR(prvi.seznam[0],drugi.seznam[0]),prvi.seznam[1])
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
        if i is not False and i is not True:
            i = i.evaluate()
        return not i
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


#razred za predstavitev XOR
class XOR:
    def __init__(self, p, q):
        self.p=p
        self.q=q
    def __repr__(self):
        return AND([OR([self.p,self.q]),NOT(AND([self.p,self.q]))]).__repr__()
    def evaluate(self):
        return AND([OR([self.p,self.q]),NOT(AND([self.p,self.q]))]).evaluate()

#razred za predstavitev EKVIVALENCE
class EQ:
	def __init(self,p,q):
		self.p=p
		self.q=q
	def __repr__(self):
		return AND([OR([NOT(self.p),self.q]),OR(NOT(self.q),self.p)]).__repr__()
	def evaluate(self):
		return AND([OR([NOT(self.p),self.q]),OR(NOT(self.q),self.p)]).evaluate()
            

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
    def flatten(self):
    	return self
    def cno(self):
    	return self

#test izpisov
##print "OSNOVNI IZPISI: true false var not and or"
##print Tru()
##print Fls()
##p = Var("p")
##print p
##print NOT(p)
##print AND([p,p])
##print OR([p,p])
##print
##
##print "SESTAVLJENA FORMULA"
##f = AND(["p", "q", OR(["p","q"])])
##print f
##print Tru()
##
##q = Var("q")
##p = Var("p")
##r = Var("r")
##
##formula = NOT(OR([AND([NOT(q), p, r]), NOT(OR([q,NOT(p),Tru()]))]))
##print formula
##print
##
###test prazen seznam vrne false
##print "PRAZEN SEZNAM"
##o = OR([])
##print o
##print
##
###testni primeri za ocenjevanje vrednosti
##print "OCENJEVANJE VREDNOSTI"
###1.
##x=Var("x")
##y=Var("y")
##v = {x: False, y: True}
##f=OR([AND([NOT(NOT(v[x])),v[y]]),NOT(v[x])])
##print "Ocena f:"
##print f
##print f.evaluate()
##print
##
#2.
##p=Var("p")
##q=Var("q")
##r=Var("r")
##u = {p: True, q: False, r: True}
##f1 = AND([OR([u[p],u[q]]),OR([u[q],u[r]]),OR([u[r],u[p]]),NOT(AND([u[p],u[q]])),NOT(AND([u[q],u[r]])),NOT(AND([u[r],u[p]]))])
##f1 = AND([OR([u[p],u[q]]),OR([u[q],u[r]]),OR([u[r],u[p]]),NOT(AND([u[p],u[q]])),NOT(AND([u[q],u[r]])),AND([u[r],u[p]])])
##print "Ocena f1:"
##print f1
##print f1.evaluate()
##print

#3.
##f2=XOR(u[p], u[r])
##print f2
##print f2.evaluate()


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
"""
p=AND([Var("a"), Var("b")])
print p.simplify()
