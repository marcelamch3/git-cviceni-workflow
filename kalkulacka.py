def kalkulacka():
    print("Jednoduchá kalkulačka")
    print("Vyber operaci:")
    print("1 - Sčítání")
    print("2 - Odčítání")
    print("3 - Násobení")
    print("4 - Dělení")

    volba = input("Zadej číslo operace (1/2/3/4): ")

    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Zadal jsi neplatné číslo.")
        return

    if volba == '1':
        print("Výsledek:", a + b)
    elif volba == '2':
        print("Výsledek:", a - b)
    elif volba == '3':
        print("Výsledek:", a * b)
    elif volba == '4':
        if b != 0:
            print("Výsledek:", a / b)
        else:
            print("Nelze dělit nulou.")

            else 
  

# Spuštění kalkulačky
kalkulacka()
