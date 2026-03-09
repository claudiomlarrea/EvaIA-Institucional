import sqlite3
import os

DB_PATH = "data/evaia.db"

def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def crear_tabla_casos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS casos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carrera TEXT,
        titulo TEXT,
        asignatura TEXT,
        desarrollo TEXT,
        pregunta1 TEXT,
        pregunta2 TEXT,
        pregunta3 TEXT,
        pregunta4 TEXT,
        diagnostico TEXT
    )
    """)

    conn.commit()
    conn.close()


def guardar_caso(carrera, titulo, asignatura, desarrollo,
                 p1, p2, p3, p4, diagnostico):

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO casos
    (carrera, titulo, asignatura, desarrollo,
     pregunta1, pregunta2, pregunta3, pregunta4, diagnostico)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (carrera, titulo, asignatura, desarrollo,
     p1, p2, p3, p4, diagnostico))

    conn.commit()
    conn.close()


def obtener_casos():

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, carrera, titulo, asignatura,
           desarrollo, pregunta1, pregunta2,
           pregunta3, pregunta4, diagnostico
    FROM casos
    """)

    casos = cur.fetchall()

    conn.close()

    return casos
