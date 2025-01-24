import streamlit as st

st.set_page_config(page_title="Condicionales en Python", page_icon="🔄")

st.title("Condicionales en Python 🔄")

st.write("""
Las estructuras condicionales permiten ejecutar diferentes bloques de código dependiendo de una condición.
""")

st.subheader("Ejemplo de código")
code = '''
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
'''
st.code(code, language='python')

st.subheader("¡Hora de practicar!")
user_code = st.text_area("Escribe una estructura condicional:", "edad = 20\nif edad > 18:\n    print('Adulto')")

if st.button("Ejecutar Código"):
    try:
        exec(user_code)
        st.success("¡Tu código se ejecutó con éxito!")
    except Exception as e:
        st.error(f"Error en el código: {e}")

# Botón de navegación
st.page_link("pages/2_variables.py", label="⬅️ Anterior: Variables", icon="👈")
st.page_link("Inicio.py", label="🏠 Volver al Inicio")
