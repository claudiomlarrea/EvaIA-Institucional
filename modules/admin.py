import streamlit as st
from database import (
    obtener_casos,
    obtener_respuestas,
    obtener_usuarios_pendientes,
    obtener_usuarios,
    actualizar_estado_usuario,
    eliminar_usuario
)


def panel_admin():
    st.header("Panel Administrador EvaIA")
    st.write("Gestión institucional de la plataforma")

    tab1, tab2, tab3 = st.tabs(["Resumen", "Usuarios", "Solicitudes pendientes"])

    with tab1:
        casos = obtener_casos()
        respuestas = obtener_respuestas()
        usuarios = obtener_usuarios()

        st.subheader("Resumen general")
        st.write(f"**Cantidad de casos cargados:** {len(casos)}")
        st.write(f"**Cantidad de respuestas enviadas:** {len(respuestas)}")
        st.write(f"**Cantidad de usuarios registrados:** {len(usuarios)}")

    with tab2:
        st.subheader("Usuarios registrados")
        usuarios = obtener_usuarios()

        if not usuarios:
            st.info("No hay usuarios registrados.")
        else:
            for u in usuarios:
                user_id, nombre, email, rol, estado, carrera, asignatura = u
                col1, col2 = st.columns([6, 1])

                with col1:
                    st.markdown(f"**{nombre}**")
                    st.write(f"Correo: {email}")
                    st.write(f"Rol: {rol}")
                    st.write(f"Estado: {estado}")
                    st.write(f"Carrera: {carrera}")
                    st.write(f"Asignatura: {asignatura}")

                with col2:
                    if rol != "admin":
                        if st.button("Eliminar", key=f"eliminar_usuario_{user_id}"):
                            eliminar_usuario(user_id)
                            st.success("Usuario eliminado")
                            st.rerun()

                st.markdown("---")

    with tab3:
        st.subheader("Solicitudes pendientes")
        pendientes = obtener_usuarios_pendientes()

        if not pendientes:
            st.info("No hay solicitudes pendientes.")
        else:
            for u in pendientes:
                user_id, nombre, email, rol, estado, carrera, asignatura = u

                st.markdown(f"### {nombre}")
                st.write(f"Correo: {email}")
                st.write(f"Rol solicitado: {rol}")
                st.write(f"Carrera: {carrera}")
                st.write(f"Asignatura: {asignatura}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Aprobar", key=f"aprobar_{user_id}"):
                        actualizar_estado_usuario(user_id, "activo")
                        st.success("Usuario aprobado correctamente")
                        st.rerun()

                with col2:
                    if st.button("Rechazar", key=f"rechazar_{user_id}"):
                        actualizar_estado_usuario(user_id, "rechazado")
                        st.warning("Usuario rechazado")
                        st.rerun()

                st.markdown("---")
