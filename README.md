						 LOGIKA V RAČUNALNIŠTVU 
						 Tinkara Toš (vpisna št)
						 Tanja Malić (27122019)
					    		Junij 2014
===================================================================================================================

OPIS:

Projekt vsebuje implementacijo podatkovnih struktur za predstavitev Boolovih formul, metode za prevedbo 
problemov na SAT obliko in algoritem za reševanje teh problemov. Uporabili smo DPLL algoritem 
(http://en.wikipedia.org/wiki/DPLL_algorithm), ki smo ga nadgradili s predhodnim sortiranjem.

DATOTEKE:

V repozitoriju se nahajajo naslednje datoteke:
- 01_boolove_formule.py: razredi za predstavitev konstant True in False, operatorjev AND, OR in NOT ter spremenljivk Var. 
   V vsakem razredu se nahaja več pomožnih metod, med drugim tudi metode za evaluacijo (klic metode z evaluate()), poenostavitve (klic metode s simplify())
   in prevedbo v CNO (klic metode s cno()). V vsaki datoteki je uvožen ta modul, tako da je povsod na voljo za uporabo.
   
- 02_redukcija_na_SAT.py: vsebuje 2 metodi, ki predstavljata prevod dveh problemov na SAT (klic metode z barvanje_grafov(graf, st_barv) in sudoku(primer_sudokuja))

- 03_DPLL.py: vsebuje metode, ki so implementacija DPLL algoritma (klic z DPLL(formula_v_cno_obliki))

NAVODILA ZA UPORABO:

Kako se ustvari konstanto, spremenljivko ali kateri koli drugi tip je prikazano v datoteki 05_primeri. Tu se nahajajo osnove
kako uporabljati strukture in klicati metode.


UNITTEST:
Tu se nahajajo testi, ki se avtomatsko zaženejo. Tu se nahajajo različni testi delovanja vseh metod ter obnašanje pri robnih primerih.
   

 
 

