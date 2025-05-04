from os.path import curdir

import pytest
import mysql.connector
from src import databaze

@pytest.fixture()
def conn():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin"
        )
        cursor = conn.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS MockTaskManager;""")
        conn.commit()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="MockTaskManager"
        )

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

        yield conn, cursor
        cursor.execute("DROP TABLE IF EXISTS ukoly;")
        conn.commit()
        cursor.close()
        conn.close()


def test_pridat_ukol(conn):
    data = ["úkol", "Popis úkolu"]
    conn, cursor = conn
    databaze.pridat_ukol(conn, data)
    dotaz = '''SELECT * FROM ukoly WHERE nazev ='úkol';'''
    cursor.execute(dotaz)
    ukoly = cursor.fetchone()

    assert ukoly is not None, "Úkol nebyl vložen do tabulky"
    assert ukoly[1] == "úkol", "Název se neshoduje."
    assert ukoly[2] == "Popis úkolu", "Popis se neshoduje"


def test_pridat_prilis_nazev_ukolu(conn, capsys):
    data = ["sssssssssssssssssssssssssssssssssssssssssssssssssss",
            "popis úkolu"]
    conn, cursor = conn
    databaze.pridat_ukol(conn, data)
    vystup = capsys.readouterr()
    porovnavac = "Přidání tasku se nepovedlo"
    assert porovnavac in vystup.out

def test_aktualizovat_ukol(conn):
    data = ["ukol", "popis ukolu"]
    conn, cursor = conn
    databaze.pridat_ukol(conn, data)
    data = ["hotovo", "1"]
    databaze.aktualizovat_ukol(conn, data)
    dotaz = "SELECT stav FROM ukoly WHERE nazev = 'ukol';"
    cursor.execute(dotaz)
    vysledek = cursor.fetchone()
    assert vysledek[0] == 'hotovo'


def test_aktualizovat_nevalidni_hodnotou(conn, capsys):
    data = ["ukol", "popis ukolu"]
    conn, cursor = conn
    databaze.pridat_ukol(conn, data)
    data = ["nehotovo", "1"]
    databaze.aktualizovat_ukol(conn, data)
    vystup = capsys.readouterr()
    assert "Update databáze se nepovedl" in vystup.out


def test_odstranit_ukol(conn):
    data = ["ukol", "popis ukolu"]
    conn, cursor = conn
    databaze.pridat_ukol(conn, data)
    data = ["1"]
    databaze.odstranit_ukol(conn, data)
    dotaz = "SELECT * FROM ukoly WHERE nazev = 'ukol';"
    cursor.execute(dotaz)
    vysledek = cursor.fetchone()
    assert vysledek is None

