from database import conectar

def inicializar_base():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS casos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carrera TEXT,
        asignatura TEXT,
        tema TEXT,
        titulo TEXT,
        dificultad TEXT,
        autor TEXT,
        desarrollo TEXT,
        consigna TEXT,
        pregunta_1 TEXT,
        pregunta_2 TEXT,
        pregunta_3 TEXT,
        pregunta_4 TEXT,
        pregunta_5 TEXT,
        respuesta_modelo TEXT,
        diagnostico_principal TEXT,
        diagnosticos_diferenciales TEXT,
        fundamentacion TEXT,
        keywords_comprension TEXT,
        keywords_aplicacion TEXT,
        keywords_razonamiento TEXT,
        keywords_hipotesis TEXT,
        keywords_fundamentacion TEXT,
        estado TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    inicializar_base()
    print("Base de datos inicializada correctamente.")
