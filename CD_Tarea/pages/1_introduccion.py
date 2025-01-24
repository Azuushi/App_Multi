import streamlit as st

st.set_page_config(page_title="Introducción a Python", page_icon="📖")

st.title("Introducción a Python 📖")

st.write("""
Python es un lenguaje de programación fácil de aprender y ampliamente utilizado en el desarrollo web, ciencia de datos e inteligencia artificial.
""")

st.subheader("Ejemplo de código")
code = '''
# Comentario en Python
print("¡Hola, mundo!")
'''
st.code(code, language='python')

st.subheader("¡Hora de practicar!")
user_code = st.text_area("Escribe tu código aquí:", "print('¡Hola, mundo!')")

if st.button("Ejecutar Código"):
    try:
        exec(user_code)
        st.success("¡Tu código se ejecutó con éxito!")
    except Exception as e:
        st.error(f"Error en el código: {e}")

# Botón de navegación
st.page_link("Inicio.py", label="⬅️ Volver al Inicio", icon="🏠")
st.page_link("pages/2_variables.py", label="Siguiente: Variables ➡️", icon="👉")
