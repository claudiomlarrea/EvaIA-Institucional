import streamlit as st
from database import autenticar_usuario


def pantalla_login():

    st.title("EvaIA")
    st.subheader("Acceso a la plataforma")

    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):

        usuario = autenticar_usuario(email, password)

        if usuario:

            st.session_state["usuario"] = usuario[1]
            st.session_state["rol"] = usuario[2]
            st.session_state["logueado"] = True

            st.rerun()

        else:
            st.error("Usuario o contraseña incorrectos")
