def hlavni_menu():
    print("""
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu""")
    return input("Vyberte možnost (1-4): ")

def pridat_ukol(ukoly):
    nazev_ukolu = input("\nZadejte název úkolu: ")
    ukol = input("Zadejte popis úkolu: ")
    ukoly.append([nazev_ukolu, ukol])
    print(f"\nÚkol {nazev_ukolu} byl přidán.")

def zobrazit_ukoly(ukoly):
    print("\nSeznam úkolů:")
    for i in ukoly:
        print(f"{(ukoly.index(i) + 1)}. {i[0]} - {i[1]}")

def odstranit_ukol(ukoly):
    zobrazit_ukoly(ukoly)
    ukol = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))
    try:
        ukoly.pop(ukol - 1)
        print(f"Úkol {ukol} byl odstraněn.")
    except:
        print("Tento úkol není v seznamu")

def konec_programu():
    print("\nKonec programu.")
    exit()

def program(ukoly):

    while True:
        volba = hlavni_menu()
        if volba == "1":
            pridat_ukol(ukoly)
    
        elif volba == "2":
            zobrazit_ukoly(ukoly)

        elif volba == "3":
            odstranit_ukol(ukoly)

        elif volba == "4":
            konec_programu()
        else:
            print("\nTato možnost není v nabídce.\nZadejte jednu z možností ze seznamu pomocí číslovek.")


ukoly = []
program(ukoly)

