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

# Zdruzljivost za Python 2 in Python 3 la
try:
    basestring
except NameError:
    basestring = str

#f je logicni izraz v KNO obliki
#literali so seznam literalov, za katere vemo vrednosti
def DPLL(f, literali):
           
    ostalo = [] #seznam ORov, kjer ne vemo vrednosti niti enega literala notri
    for i in f.seznam:
##        print "obdelujem ", i
##        print "literali ", literali
##        print "ostalo ", ostalo
        
        #dolocimo literale
        if isinstance(i, bool.Var):
##            print "je literal ", i
            if not i in literali:
                literali[i] = True
            elif not literali[i]:
                return False
        
        #dolocimo not literale
        elif isinstance(i, bool.NOT):
##            print "je not literal ", i.vrednost
            if not i.vrednost in literali:
                literali[i.vrednost] = False        
            elif literali[i.vrednost]:
                return False

        #dolocimo kar nam ostane
        else:
##            print "je ostalo ", i
            n = False
            for j in i.seznam:
                if j in literali:
                    n=True
            if not n:
                ostalo.append(i)

##    print "konec for"
##    print "literali ", literali
##    print "ostalo ", ostalo
    if len(ostalo)==0:
        return literali
    else:
        #spremenljivkam potrebno dolociti vrednosti
        #gemo kar po vrsti in recemo, da je prvi True
        #ce se ne izide s True, probamo s False
        #tako probamo za vse elemente seznama ostalo
        #ce se eden izmed elemntov seznama ostalone izide sledi ni resitve
        
        while len(ostalo)>0:
            k = ostalo[0]
            #preverimo ali se kateri izmed nastopajocih nahaja v literalih
            n = False
            for j in k.seznam:
                if j in literali:
                    n=True
            #ce se ne nahaja v literalih vstopimo v ta OR in ga resimo
            if not n:
                if isinstance(k.seznam[0], bool.NOT):
                    literali[k.seznam[0].vrednost] = True
                else:
                    literali[k.seznam[0]] = True
                true = DPLL(k, literali)
                if not true:
                    if isinstance(k.seznam[0], bool.NOT):
                        literali[k.seznam[0].vrednost] = False
                    else:
                        literali[k.seznam[0]] = False
                    true = DPLL(k, literali)
            del ostalo[0]
    return true


#testni primer
p = bool.Var('p')
q = bool.Var('q')
r = bool.Var('r')
s = bool.Var('s')
t = bool.Var('t')
u = bool.Var('u')

f_cno = bool.AND([p, bool.OR([q,r]), bool.OR([bool.NOT(r),t]), bool.OR([bool.NOT(u), p])])

print "formula: ", f_cno
##print"==============================="
res = DPLL(f_cno,{})
##print"==============================="
print "rezultat: ", res
    
    



