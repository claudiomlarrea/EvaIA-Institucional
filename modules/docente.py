import streamlit as st
from database import crear_tabla_casos, guardar_caso, obtener_casos

def panel_docente():
    st.header("Panel docente EvaIA")
    st.write("Carga de casos clínicos para aprendizaje basado en problemas")

    crear_tabla_casos()

    titulo = st.text_input("Título del caso")
    asignatura = st.text_input("Asignatura")
    caso = st.text_area("Desarrollo del caso")
    diagnostico = st.text_area("Diagnóstico esperado")

    if st.button("Guardar caso"):
        if titulo and asignatura and caso and diagnostico:
            guardar_caso(titulo, asignatura, caso, diagnostico)
            st.success("Caso guardado correctamente en la base de datos.")
        else:
            st.warning("Completá todos los campos antes de guardar.")

    st.subheader("Casos cargados")
    casos = obtener_casos()

    if casos:
        for caso_item in casos:
            st.markdown(f"**ID:** {caso_item[0]}")
            st.markdown(f"**Título:** {caso_item[1]}")
            st.markdown(f"**Asignatura:** {caso_item[2]}")
            st.markdown(f"**Desarrollo:** {caso_item[3]}")
            st.markdown(f"**Diagnóstico esperado:** {caso_item[4]}")
            st.markdown("---")
    else:
        st.info("Todavía no hay casos cargados.")
