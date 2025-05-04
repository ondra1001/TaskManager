from src import databaze


def hlavni_menu():
    print("""
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit úkoly
3. Aktualizovat úkol
4. Odstranit úkol
5. Ukončit program""")
    return input("Vyberte možnost (1-4): ")

def nazev_popis():
     while True:
        nazev = input("\nZadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")
        if nazev == "" or popis == "":
            print("\nMusíte zadat název i popis úkolu.")
        else:
            return [nazev,popis]

def stav_id():
    id = input("\nZadejte id úkolu, jehož stav chcete změnit: ")
    stav = input("\nZadejte stav úkolu (nezahájeno, probíhá, hotovo): ")
    return [stav, id]

def filtr_ukolu(conn):
    filtr = input("\nChcete filtrovat úkoly? a/n: ")
    if filtr == "a":
        vyber = [input("\nNezahájeno/probíhá: ")]
        databaze.zobrazit_filtr_ukoly(conn, vyber)
    else:
        pass


def konec_programu():
    print("\nKonec programu.")
    exit()

def main():
    databaze.vytvorit_databazi()
    conn = databaze.pripojeni_db()
    databaze.vytvorit_tabulku(conn)
    while True:
        volba = hlavni_menu()
        if volba == "1":
            data = nazev_popis()
            databaze.pridat_ukol(conn, data)

    
        elif volba == "2":
            databaze.zobrazit_ukoly(conn)
            filtr_ukolu(conn)

        elif volba == "3":
            databaze.zobrazit_ukoly(conn)
            data = stav_id()
            databaze.aktualizovat_ukol(conn, data)

        elif volba == "4":
            databaze.zobrazit_ukoly(conn)
            data = [input("Zadejte ID úkolu, který chcete smazat: ")]
            databaze.odstranit_ukol(conn, data)

        elif volba == "5":
            conn.close()
            konec_programu()
        else:
            print("\nTato možnost není v nabídce.\nZadejte jednu z možností ze seznamu pomocí číslovek.")



if __name__ == "__main__":
    main()

