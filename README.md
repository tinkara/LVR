						 LOGIKA V RAČUNALNIŠTVU 
						 Tinkara Toš (27122045)
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
   V vsakem razredu se nahaja več pomožnih metod, med drugim tudi metode za evaluacijo (klic metode z evaluate()), poenostavitve (klic metode s simplify()) in prevedbo v CNO (klic metode s cno()). V vsaki datoteki je uvožen ta modul, tako da je povsod na voljo za uporabo.
   
- 02_redukcija_na_SAT.py: vsebuje 2 metodi, ki predstavljata prevod dveh problemov na SAT (klic metode z barvanje_grafov(graf, st_barv) in sudoku(primer_sudokuja))

- 03_DPLL.py: vsebuje metode, ki so implementacija DPLL algoritma (klic z DPLL(formula_v_cno_obliki))

- 04_unit_testing.py: vsebuje teste vseh struktur, metod in DPLL algoritma
 
- 05_primeri.py: tu se nahaja prikaz uporabe vseh struktur ter klice metod in algoritma DPLL

- 05_primeri_sudoku.py: datoteka, s katero prikažemo reševanje sudoka z DPLL algoritmom

NAVODILA ZA UPORABO:

Kako se ustvari konstanto, spremenljivko ali kateri koli drugi tip je prikazano v datoteki 05_primeri. Tu se nahajajo osnove kako uporabljati strukture in klicati metode ter DPLL algoritem.

Za pregled delovanja DPLL algoritma na primeru sudoka je potrebno odpreti 05_primeri_sudoku.py in v spodnji vrstici izprati sudoku, ki ga želimo rešiti.
Za vnos novega sudoka je potrebno vnesti 

sudoku_x = 
[[None,9,2,3,4,8,1,5,7],
[7,4,3,5,None,1,9,8,2],
[8,1,5,2,9,7,None,3,4],
[5,8,None,1,2,3,7,4,9],
[4,3,1,7,8,9,5,2,None],
[2,7,9,None,5,4,8,1,3],
[9,5,8,4,7,2,3,None,1],
[1,2,7,8,3,None,4,9,5],
[3,None,4,9,1,5,2,7,8]]

(kjer je x poljubna še ne uporabljena številka), nato pa ime sudoka vpišemo v zadnjo vrstico (Sudoku_solve(sudoku_x)) in poženemo program.
Iz neznanega razloga sudoku4 ne vrne prave rešitve, ostali pa se rešijo pravilno, pri tem, da sudoku3 za rešitev potrebuje malce več časa.

UNITTEST:

Tu se nahajajo testi, ki se avtomatsko zaženejo. Vsebuje različne teste delovanja vseh metod ter obnašanje pri robnih primerih.
   

 
 

