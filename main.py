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
    ukoly.pop(ukol - 1)
    print(f"Úkol {ukol} byl odstraněn.")

def program(ukoly):
    volba = hlavni_menu()
    if volba == "1":
        pridat_ukol(ukoly)
        program(ukoly)
    elif volba == "2":
        zobrazit_ukoly(ukoly)
        program(ukoly)
    elif volba == "3":
        odstranit_ukol(ukoly)
        program(ukoly)
    elif volba == "4":
        print("\nKonec programu.")
        exit()
    else:
        print("\nTato možnost není v nabídce.\nZadejte jednu z možností ze seznamu pomocí číslovek.")
        program(ukoly)

ukoly = []
program(ukoly)

