import streamlit as st
from database import (
    guardar_caso,
    obtener_casos,
    obtener_caso_por_id,
    eliminar_caso,
    actualizar_caso
)


def panel_docente():
    st.header("Panel docente EvaIA")
    st.write("Carga y gestión de casos clínicos para aprendizaje basado en problemas")

    if "caso_editar" not in st.session_state:
        st.session_state["caso_editar"] = None

    caso_en_edicion = None
    if st.session_state["caso_editar"] is not None:
        caso_en_edicion = obtener_caso_por_id(st.session_state["caso_editar"])

    titulo_expander = "✏️ Editar caso" if caso_en_edicion else "➕ Cargar nuevo caso"

    with st.expander(titulo_expander, expanded=True):
        with st.form("form_caso"):

            carrera_default = "Medicina"
            titulo_default = ""
            asignatura_default = ""
            desarrollo_default = ""
            p1_default = ""
            p2_default = ""
            p3_default = ""
            p4_default = ""
            diagnostico_default = ""

            if caso_en_edicion:
                carrera_default = caso_en_edicion[1]
                titulo_default = caso_en_edicion[2]
                asignatura_default = caso_en_edicion[3]
                desarrollo_default = caso_en_edicion[4]
                p1_default = caso_en_edicion[5] or ""
                p2_default = caso_en_edicion[6] or ""
                p3_default = caso_en_edicion[7] or ""
                p4_default = caso_en_edicion[8] or ""
                diagnostico_default = caso_en_edicion[9] or ""

            carreras = ["Medicina", "Psicología", "Derecho"]
            index_carrera = carreras.index(carrera_default) if carrera_default in carreras else 0

            carrera = st.selectbox("Carrera", carreras, index=index_carrera)
            titulo = st.text_input("Título del caso", value=titulo_default)
            asignatura = st.text_input("Asignatura", value=asignatura_default)
            desarrollo = st.text_area("Desarrollo del caso", height=180, value=desarrollo_default)

            st.subheader("Preguntas para el estudiante")
            st.caption("La Pregunta 1 es obligatoria. Las preguntas 2, 3 y 4 son opcionales.")

            p1 = st.text_input("Pregunta 1", value=p1_default)
            p2 = st.text_input("Pregunta 2 (opcional)", value=p2_default)
            p3 = st.text_input("Pregunta 3 (opcional)", value=p3_default)
            p4 = st.text_input("Pregunta 4 (opcional)", value=p4_default)

            diagnostico = st.text_area(
                "Resolución esperada del caso (solo docente)",
                height=120,
                value=diagnostico_default
            )

            col_guardar, col_cancelar = st.columns(2)

            with col_guardar:
                texto_boton = "Actualizar caso" if caso_en_edicion else "Guardar caso"
                guardar = st.form_submit_button(texto_boton)

            with col_cancelar:
                cancelar = st.form_submit_button("Cancelar edición") if caso_en_edicion else False

            if cancelar:
                st.session_state["caso_editar"] = None
                st.rerun()

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
                if not diagnostico.strip():
                    faltantes.append("Resolución esperada")

                if faltantes:
                    st.warning("Faltan estos campos: " + ", ".join(faltantes))
                else:
                    if caso_en_edicion:
                        actualizar_caso(
                            caso_en_edicion[0],
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
                        st.session_state["caso_editar"] = None
                        st.success("Caso actualizado correctamente")
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
            col1, col2, col3, col4 = st.columns([6, 1, 1, 1])

            with col1:
                st.markdown(f"### {titulo}")
                st.write(f"Carrera: {carrera}")
                st.write(f"Asignatura: {asignatura}")

            with col2:
                if st.button("Ver", key=f"ver_{caso_id}"):
                    st.session_state["caso_ver"] = caso_id
                    st.rerun()

            with col3:
                if st.button("Editar", key=f"editar_{caso_id}"):
                    st.session_state["caso_editar"] = caso_id
                    st.rerun()

            with col4:
                if st.button("Eliminar", key=f"del_{caso_id}"):
                    eliminar_caso(caso_id)
                    if st.session_state.get("caso_ver") == caso_id:
                        del st.session_state["caso_ver"]
                    if st.session_state.get("caso_editar") == caso_id:
                        st.session_state["caso_editar"] = None
                    st.success("Caso eliminado")
                    st.rerun()

        st.markdown("---")

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
            if caso[5]:
                st.write("1.", caso[5])
            if caso[6]:
                st.write("2.", caso[6])
            if caso[7]:
                st.write("3.", caso[7])
            if caso[8]:
                st.write("4.", caso[8])

            st.markdown("### Resolución esperada del caso")
            st.write(caso[9])

            if st.button("Cerrar vista"):
                del st.session_state["caso_ver"]
                st.rerun()
