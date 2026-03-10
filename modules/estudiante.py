import streamlit as st
from database import obtener_casos, guardar_respuesta


def panel_estudiante():
    st.header("Panel Estudiante")
    st.write("Resolución de casos clínicos para aprendizaje basado en problemas")

    casos = obtener_casos()

    if not casos:
        st.info("Todavía no hay casos disponibles.")
        return

    opciones = {f"{caso[2]} ({caso[3]})": caso for caso in casos}
    seleccion = st.selectbox("Seleccioná un caso clínico", list(opciones.keys()))
    caso = opciones[seleccion]

    caso_id = caso[0]

    st.subheader(caso[2])
    st.write(f"**Carrera:** {caso[1]}")
    st.write(f"**Asignatura:** {caso[3]}")

    st.markdown("### Desarrollo del caso")
    st.write(caso[4])

    st.markdown("### Preguntas")

    estudiante = st.text_input("Nombre del estudiante", key=f"estudiante_{caso_id}")

    respuestas = {}

    if caso[5] and caso[5].strip():
        respuestas["r1"] = st.text_area(
            f"1. {caso[5]}",
            height=120,
            key=f"r1_{caso_id}"
        )
    else:
        respuestas["r1"] = ""

    if caso[6] and caso[6].strip():
        respuestas["r2"] = st.text_area(
            f"2. {caso[6]}",
            height=120,
            key=f"r2_{caso_id}"
        )
    else:
        respuestas["r2"] = ""

    if caso[7] and caso[7].strip():
        respuestas["r3"] = st.text_area(
            f"3. {caso[7]}",
            height=120,
            key=f"r3_{caso_id}"
        )
    else:
        respuestas["r3"] = ""

    if caso[8] and caso[8].strip():
        respuestas["r4"] = st.text_area(
            f"4. {caso[8]}",
            height=120,
            key=f"r4_{caso_id}"
        )
    else:
        respuestas["r4"] = ""

    if st.button("Enviar respuestas", key=f"enviar_{caso_id}"):
        faltantes = []

        if not estudiante.strip():
            faltantes.append("Nombre del estudiante")

        if caso[5] and caso[5].strip() and not respuestas["r1"].strip():
            faltantes.append("Respuesta 1")
        if caso[6] and caso[6].strip() and not respuestas["r2"].strip():
            faltantes.append("Respuesta 2")
        if caso[7] and caso[7].strip() and not respuestas["r3"].strip():
            faltantes.append("Respuesta 3")
        if caso[8] and caso[8].strip() and not respuestas["r4"].strip():
            faltantes.append("Respuesta 4")

        if faltantes:
            st.warning("Faltan estos campos: " + ", ".join(faltantes))
        else:
            guardar_respuesta(
                caso_id,
                estudiante.strip(),
                respuestas["r1"].strip(),
                respuestas["r2"].strip(),
                respuestas["r3"].strip(),
                respuestas["r4"].strip()
            )
            st.success("Respuestas enviadas correctamente")
