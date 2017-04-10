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
