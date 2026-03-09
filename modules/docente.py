import streamlit as st
from database import guardar_caso, obtener_casos


def panel_docente():
    st.header("Panel docente EvaIA")
    st.write("Carga de casos clínicos para aprendizaje basado en problemas")

    carrera = st.selectbox(
        "Carrera",
        ["Medicina", "Psicología", "Derecho"]
    )

    titulo = st.text_input("Título del caso")
    asignatura = st.text_input("Asignatura")
    desarrollo = st.text_area("Desarrollo del caso", height=180)

    st.subheader("Preguntas para el estudiante")
    p1 = st.text_input("Pregunta 1")
    p2 = st.text_input("Pregunta 2")
    p3 = st.text_input("Pregunta 3")
    p4 = st.text_input("Pregunta 4")

    diagnostico = st.text_area("Diagnóstico esperado (solo docente)", height=120)

    if st.button("Guardar caso"):
        if carrera and titulo and asignatura and desarrollo and p1 and p2 and p3 and p4 and diagnostico:
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
            st.warning("Completá todos los campos")

    st.subheader("Casos cargados")

    casos = obtener_casos()

    if casos:
        for caso in casos:
            st.markdown(f"### {caso[2]}")
            st.write(f"**Carrera:** {caso[1]}")
            st.write(f"**Asignatura:** {caso[3]}")
            st.write(f"**Desarrollo:** {caso[4]}")
            st.write(f"**Pregunta 1:** {caso[5]}")
            st.write(f"**Pregunta 2:** {caso[6]}")
            st.write(f"**Pregunta 3:** {caso[7]}")
            st.write(f"**Pregunta 4:** {caso[8]}")
            st.write(f"**Diagnóstico esperado:** {caso[9]}")
            st.markdown("---")
    else:
        st.info("Todavía no hay casos cargados.")
