import streamlit as st
from database import obtener_casos, guardar_respuesta, crear_tabla_respuestas


def panel_estudiante():

    st.header("Panel Estudiante")
    st.write("Resolución de casos clínicos para aprendizaje basado en problemas")

    crear_tabla_respuestas()

    casos = obtener_casos()

    if not casos:
        st.info("Todavía no hay casos disponibles.")
        return

    opciones = {f"{caso[2]} ({caso[3]})": caso for caso in casos}

    seleccion = st.selectbox(
        "Seleccioná un caso clínico",
        list(opciones.keys())
    )

    caso = opciones[seleccion]

    st.subheader(caso[2])
    st.write(f"Carrera: {caso[1]}")
    st.write(f"Asignatura: {caso[3]}")

    st.markdown("### Desarrollo del caso")

    st.write(caso[4])

    st.markdown("### Preguntas")

    estudiante = st.text_input("Nombre del estudiante")

    r1 = st.text_area(caso[5])
    r2 = st.text_area(caso[6])
    r3 = st.text_area(caso[7])
    r4 = st.text_area(caso[8])

    if st.button("Enviar respuestas"):

        if estudiante and r1 and r2 and r3 and r4:

            guardar_respuesta(
                caso[0],
                estudiante,
                r1,
                r2,
                r3,
                r4
            )

            st.success("Respuestas enviadas correctamente")

        else:

            st.warning("Completá nombre y todas las respuestas")
