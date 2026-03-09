import streamlit as st
from database import obtener_casos, obtener_respuestas


def panel_admin():
    st.header("Panel Administrador EvaIA")
    st.write("Gestión institucional de la plataforma")

    casos = obtener_casos()
    respuestas = obtener_respuestas()

    st.subheader("Resumen general")
    st.write(f"**Cantidad de casos cargados:** {len(casos)}")
    st.write(f"**Cantidad de respuestas enviadas:** {len(respuestas)}")

    st.subheader("Casos cargados")
    if casos:
        for caso in casos:
            st.write(f"**ID:** {caso[0]} | **Título:** {caso[2]} | **Carrera:** {caso[1]} | **Asignatura:** {caso[3]}")
    else:
        st.info("No hay casos cargados.")

    st.subheader("Respuestas enviadas")
    if respuestas:
        for r in respuestas:
            st.markdown(f"### Respuesta ID {r[0]}")
            st.write(f"**Caso ID:** {r[1]}")
            st.write(f"**Estudiante:** {r[2]}")
            st.write(f"**Respuesta 1:** {r[3]}")
            st.write(f"**Respuesta 2:** {r[4]}")
            st.write(f"**Respuesta 3:** {r[5]}")
            st.write(f"**Respuesta 4:** {r[6]}")
            st.markdown("---")
    else:
        st.info("No hay respuestas cargadas.")
