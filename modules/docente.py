import streamlit as st
from database import guardar_caso, obtener_casos, obtener_caso_por_id, eliminar_caso


def panel_docente():
    st.header("Panel docente EvaIA")
    st.write("Carga y gestión de casos clínicos para aprendizaje basado en problemas")

    # ======================================================
    # FORMULARIO DE CARGA
    # ======================================================
    with st.expander("➕ Cargar nuevo caso", expanded=True):
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
            faltantes = []

            if not carrera or not carrera.strip():
                faltantes.append("Carrera")
            if not titulo or not titulo.strip():
                faltantes.append("Título del caso")
            if not asignatura or not asignatura.strip():
                faltantes.append("Asignatura")
            if not desarrollo or not desarrollo.strip():
                faltantes.append("Desarrollo del caso")
            if not p1 or not p1.strip():
                faltantes.append("Pregunta 1")
            if not p2 or not p2.strip():
                faltantes.append("Pregunta 2")
            if not p3 or not p3.strip():
                faltantes.append("Pregunta 3")
            if not p4 or not p4.strip():
                faltantes.append("Pregunta 4")
            if not diagnostico or not diagnostico.strip():
                faltantes.append("Diagnóstico esperado")

            if faltantes:
                st.warning("Faltan estos campos: " + ", ".join(faltantes))
            else:
                guardar_caso(
                    carrera.strip(),
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

    # ======================================================
    # GESTOR DE CASOS
    # ======================================================
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
                st.write(f"**Carrera:** {carrera}")
                st.write(f"**Asignatura:** {asignatura}")

            with col2:
                if st.button("Ver", key=f"ver_{caso_id}"):
                    st.session_state["caso_ver"] = caso_id

            with col3:
                if st.button("Eliminar", key=f"eliminar_{caso_id}"):
                    eliminar_caso(caso_id)
                    if st.session_state.get("caso_ver") == caso_id:
                        del st.session_state["caso_ver"]
                    st.success("Caso eliminado correctamente")
                    st.rerun()

            st.markdown("---")

    # ======================================================
    # VISOR DE CASO
    # ======================================================
    if "caso_ver" in st.session_state:
        caso_completo = obtener_caso_por_id(st.session_state["caso_ver"])

        if caso_completo:
            st.subheader("Vista completa del caso")

            st.markdown(f"**Título:** {caso_completo[2]}")
            st.markdown(f"**Carrera:** {caso_completo[1]}")
            st.markdown(f"**Asignatura:** {caso_completo[3]}")
            st.markdown("### Desarrollo")
            st.write(caso_completo[4])

            st.markdown("### Preguntas del estudiante")
            st.write(f"**1.** {caso_completo[5]}")
            st.write(f"**2.** {caso_completo[6]}")
            st.write(f"**3.** {caso_completo[7]}")
            st.write(f"**4.** {caso_completo[8]}")

            st.markdown("### Diagnóstico esperado")
            st.write(caso_completo[9])

            if st.button("Cerrar vista del caso"):
                del st.session_state["caso_ver"]
                st.rerun()
