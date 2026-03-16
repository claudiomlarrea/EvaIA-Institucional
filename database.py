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


def guardar_caso(carrera, titulo, asignatura, desarrollo, p1, p2, p3, p4, diagnostico):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO casos
    (carrera, titulo, asignatura, desarrollo, pregunta1, pregunta2, pregunta3, pregunta4, diagnostico)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (carrera, titulo, asignatura, desarrollo, p1, p2, p3, p4, diagnostico))

    conn.commit()
    conn.close()


def actualizar_caso(caso_id, carrera, titulo, asignatura, desarrollo, p1, p2, p3, p4, diagnostico):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    UPDATE casos
    SET carrera = ?, titulo = ?, asignatura = ?, desarrollo = ?,
        pregunta1 = ?, pregunta2 = ?, pregunta3 = ?, pregunta4 = ?, diagnostico = ?
    WHERE id = ?
    """, (carrera, titulo, asignatura, desarrollo, p1, p2, p3, p4, diagnostico, caso_id))

    conn.commit()
    conn.close()


def obtener_casos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, carrera, titulo, asignatura, desarrollo, pregunta1, pregunta2, pregunta3, pregunta4, diagnostico
    FROM casos
    ORDER BY id DESC
    """)

    casos = cur.fetchall()
    conn.close()
    return casos


def obtener_caso_por_id(caso_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, carrera, titulo, asignatura, desarrollo, pregunta1, pregunta2, pregunta3, pregunta4, diagnostico
    FROM casos
    WHERE id = ?
    """, (caso_id,))

    caso = cur.fetchone()
    conn.close()
    return caso


def eliminar_caso(caso_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM casos WHERE id = ?", (caso_id,))

    conn.commit()
    conn.close()


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
    ORDER BY id DESC
    """)

    respuestas = cur.fetchall()
    conn.close()
    return respuestas

def crear_usuario(nombre, email, password, rol):

    import sqlite3

    conn = sqlite3.connect("evaia.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nombre, email, password, rol)
    VALUES (?, ?, ?, ?)
    """, (nombre, email, password, rol))

    conn.commit()
    conn.close()

def crear_usuario(nombre, email, password, rol):

    import sqlite3

    conn = sqlite3.connect("evaia.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nombre, email, password, rol)
    VALUES (?, ?, ?, ?)
    """, (nombre, email, password, rol))

    conn.commit()
    conn.close()

def autenticar_usuario(email, password):

    import sqlite3

    conn = sqlite3.connect("evaia.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nombre, rol FROM usuarios
    WHERE email=? AND password=?
    """, (email, password))

    usuario = cursor.fetchone()

    conn.close()

    return usuario


