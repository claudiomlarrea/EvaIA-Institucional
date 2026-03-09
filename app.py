import streamlit as st

# Importaciones seguras de módulos
try:
    from modules.docente import panel_docente
except Exception:
    panel_docente = None

try:
    from modules.admin import panel_admin
except Exception:
    panel_admin = None

try:
    from modules.estudiante import panel_estudiante
except Exception:
    panel_estudiante = None
    
    from database import crear_tabla_casos, crear_tabla_respuestas

crear_tabla_casos()
crear_tabla_respuestas()

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

if modo == "Estudiante":
    if panel_estudiante is not None:
        panel_estudiante()
    else:
        st.header("Panel Estudiante")
        st.warning("El módulo estudiante todavía no está disponible o tiene un error.")

elif modo == "Docente":
    if panel_docente is not None:
        panel_docente()
    else:
        st.header("Panel Docente")
        st.warning("El módulo docente todavía no está disponible o tiene un error.")

elif modo == "Administrador":
    if panel_admin is not None:
        panel_admin()
    else:
        st.header("Panel Administrador")
        st.warning("El módulo administrador todavía no está disponible o tiene un error.")
