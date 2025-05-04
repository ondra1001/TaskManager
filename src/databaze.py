import mysql.connector

def vytvorit_databazi():
    try:
        conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin"
        )
        cursor = conn.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS TaskManager;""")
        conn.commit()
        print("Databáze byla vytvořena")
    except Exception as e:
        print(f"Vytvoření databáze selhalo... {e}")


def pripojeni_db():
    try:
        conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "TaskManager"
        )
        print("Připojení k databázi proběhlo úspěšně.")
        return conn
    except Exception as e:
        print(f"Připojení k databázi selhalo..{e}")


def vytvorit_tabulku(conn):
    try:
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS ukoly (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nazev VARCHAR(50) NOT NULL,
                   popis VARCHAR(50) NOT NULL,
                   stav ENUM('nezahájeno', 'hotovo', 'probíhá') DEFAULT 'nezahájeno',
                   datum TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   );"""
        cursor.execute(query)
        conn.commit()
        print("Vytvoření tabulky proběhlo úspěšně.")
    except Exception as e:
        print(f"Vytvoření tabulky selhalo..{e}")
    finally:
        cursor.close()



def pridat_ukol(conn, data):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO ukoly(nazev, popis) VALUES(%s,%s)"""
        cursor.execute(query, data)
        conn.commit()
        print("Přidání úkolu proběhlo úspěšně.")
    except Exception as e:
        print(f"Přidání tasku se nepovedlo...{e}")
    finally:
        cursor.close()

def zobrazit_ukoly(conn):
    cursor = conn.cursor()
    dotaz = """SELECT * FROM ukoly WHERE stav = 'nezahájeno' OR stav = 'probíhá';"""
    cursor.execute(dotaz)
    ukoly = cursor.fetchall()
    try:
        if ukoly:
            print("\nSeznam úkolů")
            for ukol in ukoly:
                print(f"\nID úkolu: {ukol[0]} | název: {ukol[1]} | popis: {ukol[2]} | stav: {ukol[3]}")
        else:
            print("Seznam je prázdný.")
    except Exception as e:
        print(f"Operace selhala..{e}")
    finally:
        cursor.close()

def zobrazit_filtr_ukoly(conn, vyber):
    cursor = conn.cursor()
    dotaz = """SELECT * FROM ukoly WHERE stav = %s;"""
    cursor.execute(dotaz, vyber)
    ukoly = cursor.fetchall()
    try:
        for ukol in ukoly:
            print(f"\nID úkolu: {ukol[0]} | název: {ukol[1]} | popis: {ukol[2]} | stav: {ukol[3]}")
    except Exception as e:
        print(f"Operace selhala...{e}")

def aktualizovat_ukol(conn, data):
    try:
        cursor = conn.cursor()
        dotaz = """UPDATE ukoly
            SET stav = %s
            WHERE id = %s;"""
        cursor.execute(dotaz, data)
        conn.commit()
        print("Záznam byl aktualizován..")
    except Exception as e:
        print(f"Update databáze se nepovedl...{e}")
    finally:
        cursor.close()


def odstranit_ukol(conn, data):
    try:
        cursor = conn.cursor()
        dotaz = """DELETE FROM ukoly WHERE id = %s;"""
        cursor.execute(dotaz, data)
        conn.commit()
        print("Záznam byl smazán.")
    except Exception as e:
        print(f"Záznam se nepodařilo smazat...{e}")
    finally:
        cursor.close()






    
