#05 Zadani prikazu s cyklem for a funkci range(), ktery vypise 4x a pod sebou.
print("Ukol 05")
for i in range (4):
  print("a")

print()

#06 Napíše pod sebe "Řádek 0" až "Řádek 4"
print("Ukol 06")
for cislo_radku in range (5):
  print("Řádek ",cislo_radku)

print()

#08 Cyklus for postupne napise, kolik je 0-4 na druhou.
print("Ukol 08")
for i in range(5):
    print(i," na druhou je ",i**2)

print()

#09 Pomoci cyklu program napise 5 radku s peti X vedle sebe.
print("Ukol 09")
for pocet_radku in range(5):
    for pocet_znaku in range(5):
        print("X", end=' ')
    print()

print()

#10 Vypise tabulku s nasobilkou - 1. radek nasobky 0, 2. radek nasobky 1,...,5. radek nasobky 4.
print("Ukol 10")
nasobek=0
for pocet_radku in range(5):
    for pocet_cisel in range(5):
        print(nasobek*pocet_cisel,end=" ")
    nasobek=nasobek+1
    print()

print()

#11 Pomoci cyklu program napise 4 radky, na kterych budu postupne jedno az ctyri X vedle sebe.
print("Ukol 11")
znak=1
for pocet_radku in range(4):
    for pocet_znaku in range(znak):
        print("X", end=' ')
    znak=znak+1
    print()

print()

#12 Pomocí cyklu for a příkazu if napíše program, který vypíše první řádek a u ostatních napíše, že není první.
print("Ukol 12")
for i in range(5):
    if i == 0:
        print("první řádek")
    else:
        print("není první")

print()

#13 Pomocí cyklů for a příkazu if napiš program, který z jednotlivých "x" a mezer vypíše čtverec (první řádek je z X, další řádky mají X jako první a poslední znak a poslední řádek je z X).
print("Ukol 13")
for cislo_radku in range(6):
    for pozice_v_radku in range(7):
        if (cislo_radku == 0) or (cislo_radku == 5) or (pozice_v_radku == 0) or (pozice_v_radku == 6):
            print("X ", end = "")
        else:
            print("  ", end = "")
    print()

print()

#14 Předchozí úkoly, u kterých je uživatel vyzván k zadání počtu opakování řádků (velikosti čtverce/trojúhelníku...)
print("Ukol 14-09")
pocet_x = int(input("Zadej počet X ve sloupci/řádku: "))
cislo_je_spravne = pocet_x > 0
if cislo_je_spravne:
    for pocet_radku in range(pocet_x):
        for pocet_znaku in range(pocet_x):
            print("X", end=' ')
        print()
else:
        print("Zadej celé číslo větší než nula.")
        print('Spusť příkaz znovu a zadej správnou hodnotu.')
print()

print("Ukol 14-11")
radek = int(input("Zadej počet řádků: "))
znak=1
cislo_je_spravne = radek > 0
if cislo_je_spravne:
    for pocet_radku in range(radek):
        for pocet_znaku in range(znak):
            print("X", end=' ')
        znak=znak+1
        print()
else:
        print("Zadej celé číslo větší než nula.")
        print('Spusť příkaz znovu a zadej správnou hodnotu.')
print()

#Cvičné příklady k úlohám 14 - 17 - pokud dám print pro proměnnou s rozsahem řetězec, pak se každý znak řetězce vyprintuje pod sebe.
for k in "Ahoj svete!":
    print(k)
print()
for l in "abcdef":
    print(l)
print()
for m in "a,b,c,d,e,f":
    print(m)
print()
for n in "1234":
    print(n)
print()
for o in "1,2,3,4":
    print(o)

print()

#19 Zepta se na 3 cisla a zjisti, zda je jejich soucet vetsi nez 10.
print("Ukol 19")
a = int(input("Zadej celé kladné číslo mezi 0 a 5: "))
b = int(input("Zadej celé kladné číslo mezi 0 a 5: "))
c = int(input("Zadej celé kladné číslo mezi 0 a 5: "))
soucet = a+b+c

if a > 5 or b > 5 or c > 5:
    print("Bylo zadáno číslo větší než 5. Spusť příkaz znovu a zadej správná čísla.")

else:
    if soucet > 10:
        print("Součet čísel je větší než 10.")
    else:
        print("Součet čísel není větší než 10.")
print()

#20 Nacte cislo a zjisti, zda je sude nebo liche.
print("Ukol 20")
from random import randrange, random, randint

cislo = randrange (100)
if cislo % 2 == 0:
    print("Počítač vybral číslo ",cislo,"a toto číslo je sudé.")
else:
    print("Počítač vybral číslo ",cislo,"a toto číslo je liché.")

print()

#22_faktorial Zepta se na cele kladne cislo mezi 0 a 10 a vypise radu do faktorialu daneho cisla.
print("Ukol 22 - faktorial")
cislo = int(input("Zadej celé kladné číslo od 0 do 10. Program spočítá jeho faktoriál."))+1
if cislo < 0 or cislo > 10:
    print("Bylo zadáno číslo mimo zadaný rozsah. Zkus to znovu")
elif cislo == 0:
    print("Faktoriál čísla ", cislo, " je 1.")
else:
    faktorial = 1
    for i in range(1,cislo):
        faktorial = faktorial * i
        print(faktorial)
print()

#22_prvocislo Zepta se na cele kladne cislo a zjisti, zda je prvocislo.
print("Ukol 22 - prvocislo")
n = int(input("Zadej celé kladné číslo. Program zjistí, zda se jedná o prvočíslo."))
if n == 2:
    print("Zvolené číslo ",n," je prvočíslo.")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    print("Zvolené číslo ",n," není prvočíslo.")

else:
    print("Zvolené číslo ",n," je prvočíslo.")

print()

#22_Fibonacciho posloupnost Vypise pocet kraliku na konci daneho mesice - Fibonacciho posloupnost (1,1,2,3,5,8,13,21...)
#První měsíc se narodí jediný pár.
#Nově narozené páry jsou produktivní od druhého měsíce svého života.
#Každý měsíc zplodí každý produktivní pár jeden další pár.
#Králíci nikdy neumírají, nejsou nemocní atd.

print("Ukol 22 - Fibonacci")

mesic = int(input("Zadej celé kladné číslo, které určí měsíc od narození prvního páru králíků."))
while mesic < 1:
    print("Zvolené číslo je mimo požadovaný rozsah.  ")
    mesic = int(input("Zadej celé kladné číslo, které určí měsíc od narození prvního páru králíků."))

if mesic == 1:

    print("V prvním měsíci žije 1 pár králíků a zatím to jsou neplodné děti.")

else:
    minuly_mesic = 1
    aktualni_mesic = 1

    for i in range(mesic):
        print(minuly_mesic)
        dalsi_mesic = minuly_mesic + aktualni_mesic
        minuly_mesic = aktualni_mesic
        aktualni_mesic = dalsi_mesic
print()
