import streamlit as st
from modules.docente import panel_docente
from modules.admin import panel_admin

st.set_page_config(
    page_title="EvaIA UCCuyo",
    page_icon="🧠",
    layout="wide"
)

st.title("EvaIA")
st.subheader("Observatorio de Inteligencia Artificial - Universidad Católica de Cuyo")

st.write("Plataforma institucional de aprendizaje basado en problemas.")

modo = st.sidebar.radio(
    "Seleccioná un modo",
    ["Estudiante", "Docente", "Administrador"]
)

if modo == "Estudiante":
    st.header("Panel Estudiante")
    st.write("Módulo de resolución de casos en construcción.")

elif modo == "Docente":
    panel_docente()

elif modo == "Administrador":
    panel_admin()
