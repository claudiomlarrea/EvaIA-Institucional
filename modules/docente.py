import streamlit as st
from database import guardar_caso, obtener_casos, obtener_caso_por_id, eliminar_caso


def panel_docente():

    st.header("Panel docente EvaIA")
    st.write("Carga y gestión de casos clínicos para aprendizaje basado en problemas")

    # =====================================================
    # FORMULARIO DE CARGA
    # =====================================================

    with st.expander("➕ Cargar nuevo caso", expanded=True):

        with st.form("form_caso"):

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

            diagnostico = st.text_area(
                "Resolución esperada del caso (solo docente)",
                height=120
            )

            guardar = st.form_submit_button("Guardar caso")

            if guardar:

                faltantes = []

                if not titulo.strip():
                    faltantes.append("Título")

                if not asignatura.strip():
                    faltantes.append("Asignatura")

                if not desarrollo.strip():
                    faltantes.append("Desarrollo")

                if not p1.strip():
                    faltantes.append("Pregunta 1")

                if not p2.strip():
                    faltantes.append("Pregunta 2")

                if not p3.strip():
                    faltantes.append("Pregunta 3")

                if not p4.strip():
                    faltantes.append("Pregunta 4")

                if not diagnostico.strip():
                    faltantes.append("Diagnóstico")

                if faltantes:
                    st.warning("Faltan estos campos: " + ", ".join(faltantes))

                else:

                    guardar_caso(
                        carrera,
                        titulo.strip(),
                        asignatura.strip(),
                        desarrollo.strip(),
                        p1.strip(),
                        p2.strip(),
                        p3.strip(),
                        p4.strip(),
                        diagnostico.strip()
                    )

                    st.success("Caso guardado correctamente")
                    st.rerun()

    st.divider()

    # =====================================================
    # GESTOR DE CASOS
    # =====================================================

    st.subheader("Gestor de casos")

    casos = obtener_casos()

    if not casos:
        st.info("Todavía no hay casos cargados.")
        return

    for caso in casos:

        caso_id = caso[0]
        carrera = caso[1]
        titulo = caso[2]
        asignatura = caso[3]

        with st.container():

            col1, col2, col3 = st.columns([6, 1, 1])

            with col1:
                st.markdown(f"### {titulo}")
                st.write(f"Carrera: {carrera}")
                st.write(f"Asignatura: {asignatura}")

            with col2:
                if st.button("Ver", key=f"ver_{caso_id}"):
                    st.session_state["caso_ver"] = caso_id

            with col3:
                if st.button("Eliminar", key=f"del_{caso_id}"):
                    eliminar_caso(caso_id)
                    st.success("Caso eliminado")
                    st.rerun()

        st.markdown("---")

    # =====================================================
    # VISOR DE CASO
    # =====================================================

    if "caso_ver" in st.session_state:

        caso = obtener_caso_por_id(st.session_state["caso_ver"])

        if caso:

            st.subheader("Vista completa del caso")

            st.markdown(f"**Título:** {caso[2]}")
            st.markdown(f"**Carrera:** {caso[1]}")
            st.markdown(f"**Asignatura:** {caso[3]}")

            st.markdown("### Desarrollo")
            st.write(caso[4])

            st.markdown("### Preguntas")

            st.write("1.", caso[5])
            st.write("2.", caso[6])
            st.write("3.", caso[7])
            st.write("4.", caso[8])

            st.markdown("### Diagnóstico esperado")
            st.write(caso[9])

            if st.button("Cerrar vista"):
                del st.session_state["caso_ver"]
                st.rerun()
