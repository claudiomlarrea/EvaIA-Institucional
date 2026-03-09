import streamlit as st
from database import crear_tabla_casos, guardar_caso, obtener_casos

def panel_docente():

    st.header("Panel docente EvaIA")
    st.write("Carga de casos clínicos para aprendizaje basado en problemas")

    crear_tabla_casos()

    carrera = st.selectbox(
        "Carrera",
        ["Medicina", "Psicología", "Derecho"]
    )

    titulo = st.text_input("Título del caso")

    asignatura = st.text_input("Asignatura")

    desarrollo = st.text_area("Desarrollo del caso")

    st.subheader("Preguntas para el estudiante")

    p1 = st.text_input("Pregunta 1")
    p2 = st.text_input("Pregunta 2")
    p3 = st.text_input("Pregunta 3")
    p4 = st.text_input("Pregunta 4")

    diagnostico = st.text_area("Diagnóstico esperado (solo docente)")

    if st.button("Guardar caso"):

        if titulo and asignatura and desarrollo:

            guardar_caso(
                carrera,
                titulo,
                asignatura,
                desarrollo,
                p1,
                p2,
                p3,
                p4,
                diagnostico
            )

            st.success("Caso guardado correctamente")

        else:

            st.warning("Completá los campos obligatorios")

    st.subheader("Casos cargados")

    casos = obtener_casos()

    if casos:

        for caso in casos:

            st.markdown(f"### {caso[2]}")
            st.markdown(f"Carrera: {caso[1]}")
            st.markdown(f"Asignatura: {caso[3]}")
            st.markdown("---")

    else:

        st.info("Todavía no hay casos cargados.")
