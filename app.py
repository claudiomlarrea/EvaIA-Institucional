import streamlit as st
from modules.docente import panel_docente
from modules.admin import panel_admin
from modules.estudiante import panel_estudiante

st.set_page_config(
    page_title="EvaIA UCCuyo",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}

.evaia-header {
    background: linear-gradient(90deg, #0B4F8A 0%, #1669B2 100%);
    padding: 18px 22px;
    border-radius: 12px;
    color: white;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

.evaia-header h1 {
    margin: 0;
    font-size: 30px;
    font-weight: 700;
}

.evaia-header p {
    margin: 4px 0 0 0;
    font-size: 15px;
}

.stButton > button,
.stDownloadButton > button {
    background-color: #0B4F8A !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 0.5rem 1rem !important;
    font-weight: 600 !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #083A66 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

def mostrar_encabezado():
    st.markdown(
        """
        <div class="evaia-header">
            <h1>EvaIA</h1>
            <p>Plataforma de aprendizaje basado en problemas con inteligencia artificial</p>
            <p><strong>Universidad Católica de Cuyo</strong> · Observatorio de Inteligencia Artificial</p>
        </div>
        """,
        unsafe_allow_html=True
    )

mostrar_encabezado()

modo = st.sidebar.radio(
    "Seleccioná un modo",
    ["Estudiante", "Docente", "Administrador"]
)

if modo == "Estudiante":
    panel_estudiante()

elif modo == "Docente":
    panel_docente()

elif modo == "Administrador":
    panel_admin()
