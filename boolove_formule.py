###################################################################
#                            VAJA 1                               #
#  naloga 1 - podatkovna struktura za Boolove formule             #
#  naloga 2 - funkcija/metoda, ki vrne vrednost Boolove formule   #
#  naloga 3 - funkcija/metoda za poenostavljanje izrazov          #
###################################################################


#razred za predstavitev konstante T
class Tru():
    def __init__(self):
        pass
    def __str__(self):
        return 'T'

#razred za predstavitev konstante F
class Fls():
    def __init__(self):
        pass
    def __str__(self):
        return 'F'

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
        
#razred za predstavitev NEG
class NOT:
    def __init__(self, ime):
        self.ime=ime
    def __repr__(self):
        return '¬ ' + str(self.ime)

#razred za predstavitev spremenljivke
class Var:
    def __init__(self, ime):
        self.ime=ime
    def __str__(self):
        return self.ime




#testni primeri
v = Var("p")
print v
n = NOT(v)
print n
f = AND(["p", "q", OR(["p","q"])])
print f
print Tru()

q = Var("q")
p = Var("p")
r = Var("r")

formula = NOT(OR([AND([NOT(q), p, r]), NOT(OR([q,NOT(p),Tru()]))]))
print formula

f = OR(Var("p"),Var("q"))(OR(Var("q"),Var("r"))
print f

o = OR([])
print o

