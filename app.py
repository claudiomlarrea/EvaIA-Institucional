import streamlit as st
from database import (
    crear_tabla_casos,
    crear_tabla_respuestas,
    crear_tabla_usuarios,
    crear_admin_inicial
)
from modules.docente import panel_docente
from modules.admin import panel_admin
from modules.estudiante import panel_estudiante
from modules.login import pantalla_login
from modules.registro import pantalla_registro

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="EvaIA UCCuyo",
    page_icon="🧠",
    layout="wide"
)

# Crear tablas si no existen
crear_tabla_casos()
crear_tabla_respuestas()
crear_tabla_usuarios()

# Crear admin inicial solo si no existe ninguno
crear_admin_inicial(
    "Administrador EvaIA",
    "admin@evaia.com",
    "admin123"
)

# Estado de sesión
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

if "rol" not in st.session_state:
    st.session_state["rol"] = ""

if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "login"

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

if not st.session_state["logueado"]:
    if st.session_state["pantalla"] == "login":
        pantalla_login()
    elif st.session_state["pantalla"] == "registro":
        pantalla_registro()
else:
    st.sidebar.markdown("### Usuario")
    st.sidebar.write(st.session_state["usuario"])
    st.sidebar.markdown("### Rol")
    st.sidebar.write(st.session_state["rol"])

    if st.sidebar.button("Cerrar sesión"):
        st.session_state.clear()
        st.rerun()

    rol = st.session_state["rol"]

    if rol == "estudiante":
        panel_estudiante()

    elif rol == "docente":
        panel_docente()

    elif rol == "admin":
        panel_admin()

    else:
        st.error("Rol no reconocido.")
