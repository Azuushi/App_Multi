import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Curso de Python Básico", page_icon="🐍", layout="wide")

# Estilización personalizada con HTML y CSS
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 45px;
            color: #4CAF50;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #ffffff;
        }
        .info-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 18px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título centrado con estilos mejorados
st.markdown('<p class="title">🐍 Bienvenido al Curso de Python Básico 🐍</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aprende los fundamentos de Python de manera interactiva y práctica.</p>', unsafe_allow_html=True)

# Crear columnas para una mejor distribución
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("https://www.python.org/static/community_logos/python-logo.png", use_container_width=True)

# Caja informativa con un diseño elegante
st.markdown('<div class="info-box">Práctica 1_MultiPages_YamFalcon.</div>', unsafe_allow_html=True)

st.info("¡Explora Python paso a paso y practica con ejercicios interactivos!")

# Botón centrado con margen superior
st.markdown('<div class="button-container">', unsafe_allow_html=True)
st.page_link("pages/1_introduccion.py", label="Ir a Introducción ➡️", icon="👉")
st.markdown('</div>', unsafe_allow_html=True)
