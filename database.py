import sqlite3
import os

DB_PATH = "data/evaia.db"

def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def crear_tabla_casos():
    conn = conectar()
    cur = conn.cursor()

    # BORRA la tabla anterior si existía con otra estructura
    cur.execute("DROP TABLE IF EXISTS casos")

    cur.execute("""
    CREATE TABLE casos (
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

def crear_tabla_respuestas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS respuestas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        caso_id INTEGER,
        estudiante TEXT,
        respuesta1 TEXT,
        respuesta2 TEXT,
        respuesta3 TEXT,
        respuesta4 TEXT
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

def guardar_respuesta(caso_id, estudiante, r1, r2, r3, r4):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO respuestas
    (caso_id, estudiante, respuesta1, respuesta2, respuesta3, respuesta4)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (caso_id, estudiante, r1, r2, r3, r4))

    conn.commit()
    conn.close()

def obtener_respuestas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, caso_id, estudiante, respuesta1, respuesta2, respuesta3, respuesta4
    FROM respuestas
    """)

    respuestas = cur.fetchall()

    conn.close()
    return respuestas
