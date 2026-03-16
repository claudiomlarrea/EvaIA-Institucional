import sqlite3
import os

DB_PATH = "data/evaia.db"


def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


# =========================================================
# TABLAS
# =========================================================

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


def crear_tabla_usuarios():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        rol TEXT NOT NULL,
        estado TEXT NOT NULL,
        carrera TEXT,
        asignatura TEXT
    )
    """)

    conn.commit()
    conn.close()


# =========================================================
# CASOS
# =========================================================

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


# =========================================================
# RESPUESTAS
# =========================================================

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


# =========================================================
# USUARIOS
# =========================================================

def registrar_usuario(nombre, email, password, rol, carrera, asignatura):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO usuarios (nombre, email, password, rol, estado, carrera, asignatura)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nombre, email, password, rol, "pendiente", carrera, asignatura))

    conn.commit()
    conn.close()


def autenticar_usuario(email, password):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, nombre, rol, estado
    FROM usuarios
    WHERE email = ? AND password = ?
    """, (email, password))

    usuario = cur.fetchone()
    conn.close()
    return usuario


def obtener_usuarios():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, nombre, email, rol, estado, carrera, asignatura
    FROM usuarios
    ORDER BY id DESC
    """)

    usuarios = cur.fetchall()
    conn.close()
    return usuarios


def obtener_usuarios_pendientes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, nombre, email, rol, estado, carrera, asignatura
    FROM usuarios
    WHERE estado = 'pendiente'
    ORDER BY id DESC
    """)

    usuarios = cur.fetchall()
    conn.close()
    return usuarios


def actualizar_estado_usuario(usuario_id, nuevo_estado):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    UPDATE usuarios
    SET estado = ?
    WHERE id = ?
    """, (nuevo_estado, usuario_id))

    conn.commit()
    conn.close()


def eliminar_usuario(usuario_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))

    conn.commit()
    conn.close()


def existe_admin():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM usuarios
    WHERE rol = 'admin'
    """)

    cantidad = cur.fetchone()[0]
    conn.close()
    return cantidad > 0


def crear_admin_inicial(nombre, email, password):
    if existe_admin():
        return

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO usuarios (nombre, email, password, rol, estado, carrera, asignatura)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nombre, email, password, "admin", "activo", "Administración", "EvaIA"))

    conn.commit()
    conn.close()
