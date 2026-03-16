import sqlite3
import streamlit as st
from database import registrar_usuario


def pantalla_registro():
    st.title("Registro de usuario")
    st.write("Completá este formulario para solicitar acceso a EvaIA.")

    nombre = st.text_input("Nombre y apellido")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    confirmar = st.text_input("Confirmar contraseña", type="password")

    rol = st.selectbox("Rol solicitado", ["estudiante", "docente"])
    carrera = st.selectbox("Carrera", ["Medicina", "Psicología", "Derecho"])
    asignatura = st.text_input("Asignatura")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Enviar solicitud de registro"):
            faltantes = []

            if not nombre.strip():
                faltantes.append("Nombre y apellido")
            if not email.strip():
                faltantes.append("Correo electrónico")
            if not password.strip():
                faltantes.append("Contraseña")
            if not confirmar.strip():
                faltantes.append("Confirmación de contraseña")
            if not asignatura.strip():
                faltantes.append("Asignatura")

            if faltantes:
                st.warning("Faltan estos campos: " + ", ".join(faltantes))
            elif password != confirmar:
                st.error("Las contraseñas no coinciden")
            else:
                try:
                    registrar_usuario(
                        nombre.strip(),
                        email.strip(),
                        password.strip(),
                        rol,
                        carrera,
                        asignatura.strip()
                    )
                    st.success("Solicitud enviada correctamente. Quedará pendiente de aprobación.")
                except sqlite3.IntegrityError:
                    st.error("Ese correo ya está registrado.")

    with col2:
        if st.button("Volver al login"):
            st.session_state["pantalla"] = "login"
            st.rerun()
