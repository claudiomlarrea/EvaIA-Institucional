import streamlit as st
from database import autenticar_usuario


def pantalla_login():
    st.title("EvaIA")
    st.subheader("Acceso a la plataforma")

    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ingresar"):
            usuario = autenticar_usuario(email.strip(), password.strip())

            if not usuario:
                st.error("Usuario o contraseña incorrectos")
            else:
                user_id, nombre, rol, estado = usuario

                if estado != "activo":
                    st.warning("Tu usuario todavía no está activo. Esperá la aprobación del administrador.")
                else:
                    st.session_state["logueado"] = True
                    st.session_state["usuario_id"] = user_id
                    st.session_state["usuario"] = nombre
                    st.session_state["rol"] = rol
                    st.rerun()

    with col2:
        if st.button("Quiero registrarme"):
            st.session_state["pantalla"] = "registro"
            st.rerun()
