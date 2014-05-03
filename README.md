						 LOGIKA V RAČUNALNIŠTVU 
						 Tinkara Toš (vpisna št)
						 Tanja Malić (27122019)
					    		Junij 2014
===================================================================================================================

Projekt vsebuje implementacijo podatkovnih struktur za predstavitev Boolovih formul, metode za prevedbo 
problemov na SAT obliko in algoritem za reševanje teh problemov. Uporabili smo DPLL algoritem 
(http://en.wikipedia.org/wiki/DPLL_algorithm), ki smo ga nadgradili s predhodnim sortiranjem.

DATOTEKE:
V repozitoriju se nahajajo naslednje datoteke:
- 01_boolove_formule.py: razredi za predstavitev konstant True in False, operatorjev AND, OR in NOT ter spremenljivk Var. 
   V vsakem razredu se nahaja več pomožnih metod, med drugim tudi metode za evaluacijo, poenostavitve in prevedbo v CNO.
   
- 02_redukcija_na_SAT.py: vsebuje 2 metodi, ki predstavljata prevod dveh problemov na SAT (problem barvanja_grafov in sudoku)

- 03_DPLL.py: vsebuje 1 metodo, ki je implementacija DPLL algoritma

NAVODILA ZA UPORABO:
Sprehod skozi datoteko s primeri da vedeti kako se lahko implementirano uporablja.

UNITTEST:


   

 
 

