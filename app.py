import streamlit as st
from modules.docente import panel_docente
from modules.admin import panel_admin

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="EvaIA UCCuyo",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================
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

.subbox {
    background-color: white;
    padding: 14px 16px;
    border-radius: 10px;
    border-left: 5px solid #0B4F8A;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    margin-bottom: 12px;
}

.metric-box {
    background-color: white;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
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

div[data-testid="stForm"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 5px rgba(0,0,0,0.05);
}

.small-note {
    color: #4B5563;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# ENCABEZADO
# =========================================================
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

# =========================================================
# INTERFAZ PRINCIPAL
# =========================================================
mostrar_encabezado()

modo = st.sidebar.radio(
    "Seleccioná un modo",
    ["Estudiante", "Docente", "Administrador"]
)

# =========================================================
# MODO ESTUDIANTE
# =========================================================
if modo == "Estudiante":
    st.header("Panel Estudiante")
    st.write("Módulo de resolución de casos en construcción.")

# =========================================================
# MODO DOCENTE
# =========================================================
elif modo == "Docente":
    panel_docente()

# =========================================================
# MODO ADMINISTRADOR
# =========================================================
elif modo == "Administrador":
    panel_admin()
