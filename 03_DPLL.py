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
#literali so seznam literalov, za katere vemo vrednosti (in se ne smejo spreminjati)
#lahkoDodajamoVLiterale je True/False vrednost, ki pove ali smem spr spreminjati (ce da, je ne smem dati v literale)
def DPLL_alg(f, literali, lahkoDodajamVLiterale):
    ostalo = [] #seznam ORov, kjer ne vemo vrednosti niti enega literala notri
    for i in f.seznam:
      
        #dolocimo literale
        if isinstance(i, bool.Var):
            if not str(i) in literali and lahkoDodajamVLiterale:
                literali[str(i)] = True
            elif str(i) in literali:
                if not literali[str(i)]:
                    return False
        
        #dolocimo not literale
        elif isinstance(i, bool.NOT):
            if not str(i.vrednost) in literali and lahkoDodajamVLiterale:
                literali[str(i.vrednost)] = False
            elif str(i.vrednost) in literali:
                if literali[str(i.vrednost)]:
                    return False

        #dolocimo kar nam ostane
        else:
            vSeznamuLiteralov = False
            for j in i.seznam:
                if isinstance(j, bool.Var) and str(j) in literali:
                    if literali[str(j)]:
                        vSeznamuLiteralov=True
            if not vSeznamuLiteralov:
                ostalo.append(i)
    
    if len(ostalo)==0:
        return literali
    #spremenljivkam potrebno dolociti vrednosti - BF
    else:        
        seLahkoSpremeni = []    #seznam, ki hrani tiste spr, ki jih lahko spreminjamo   
        niResitve = False
        while len(ostalo)>0 and not niResitve:
            k = ostalo[0]
            #preverimo ali se kateri izmed nastopajocih nahaja v literalih
            #ali ce je sestavljena iz samih NOT
            #ustvarimo nov (poenostavljen) OR seznam
            vSeznamuLiteralov = False
            or_seznam = []
            count = 0
            for j in k.seznam:
                if isinstance(j, bool.Var):
                    if str(j) in literali:
                        vSeznamuLiteralov=True
                    elif str(j) not in seLahkoSpremeni :
                        seLahkoSpremeni.append(str(j))
                    or_seznam.append(j)
                elif isinstance(j, bool.NOT):
                    if str(j.vrednost) in literali:
                        if literali[str(j.vrednost)]:
                            count += 1
                    elif str(j.vrednost) not in seLahkoSpremeni:
                        seLahkoSpremeni.append(str(j.vrednost))
                        or_seznam.append(j)
                if vSeznamuLiteralov and not DPLL_alg(bool.OR([j]),literali,False):
                    niResitve = True
                elif vSeznamuLiteralov:
                    or_seznam = []
            
            if count==len(k.seznam):    #sami NOT, ki imajo znane literale, sledi ni resitve
                niResitve = True
           
            else:
                k=bool.OR(or_seznam)
                if (not vSeznamuLiteralov) and not niResitve and len(k.seznam)!=0:
                    key = k.seznam[0]
                    keyNOT=""
                    if isinstance(key, bool.NOT):
                        keyNOT = str(k.seznam[0].vrednost)
                    true = ""
                    if isinstance(key, bool.NOT) and str(keyNOT) in seLahkoSpremeni:
                        literali[keyNOT] = True
                        true = DPLL_alg(k, literali, False)
                    elif str(key) in seLahkoSpremeni:
                        literali[str(key)] = True
                        true = DPLL_alg(k, literali, False)
                    if not true:
                        if isinstance(key, bool.NOT) and str(keyNOT) in seLahkoSpremeni:
                            literali[keyNOT] = False
                            true = DPLL_alg(k, literali, False)
                        elif str(key) in seLahkoSpremeni:
                            literali[str(key)] = False
                            true = DPLL_alg(k, literali, False)
                del ostalo[0]
        if niResitve:
            return False
        else:
            return literali


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
    #print "formula sorted: ", f_cno_sorted
    return DPLL_alg(f_cno_sorted,{}, True)


#Metoda, ki pozene klic sortiranja (tam pa se pozene algoritem).
#Argument je formula f v CNO.
def DPLL(f):
    res = DPLL_sort(f)
    if not res:
        return "Ni Resitve."
    else:
        return res
    
    



