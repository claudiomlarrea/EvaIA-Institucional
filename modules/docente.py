import streamlit as st

def panel_docente():
    st.header("Panel docente EvaIA")
    st.write("Carga de casos clínicos para aprendizaje basado en problemas")

    titulo = st.text_input("Título del caso")
    asignatura = st.text_input("Asignatura")
    caso = st.text_area("Desarrollo del caso")
    diagnostico = st.text_area("Diagnóstico esperado")

    if st.button("Guardar caso"):
        st.success("Caso guardado (versión piloto)")
