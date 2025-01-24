import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Variables en Python", page_icon="🧮")

st.title("Variables en Python 🧮")

st.write("""
Las variables son contenedores para almacenar valores. 
En Python no necesitas especificar el tipo de dato.
""")

# Mostrar ejemplo de código
st.subheader("Ejemplo de código")
code = '''
nombre = "Alice"
edad = 25
altura = 1.75

print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura} m")
'''
st.code(code, language='python')

# Sección para que el usuario practique
st.subheader("¡Hora de practicar!")
st.write("Define tus propias variables y prueba:")

# Área de texto para ingresar código
user_code = st.text_area("Escribe tu código aquí:", "nombre = 'Carlos'\nprint(nombre)", height=150)

# Espacio para mostrar los resultados
output_placeholder = st.empty()

# Botón para ejecutar el código
if st.button("Ejecutar Código"):
    try:
        # Capturar salida del código
        import io
        import sys

        output = io.StringIO()
        sys.stdout = output  # Redirigir la salida estándar a la variable 'output'

        exec(user_code)  # Ejecutar el código ingresado por el usuario

        sys.stdout = sys.__stdout__  # Restaurar la salida estándar
        result = output.getvalue()  # Obtener la salida capturada

        # Mostrar resultado debajo del botón
        output_placeholder.success("¡Tu código se ejecutó con éxito!")
        st.code(result, language='python')  # Mostrar el resultado del código ejecutado

    except Exception as e:
        sys.stdout = sys.__stdout__  # Restaurar la salida estándar en caso de error
        output_placeholder.error(f"Error en el código: {e}")

# Botones de navegación
st.page_link("pages/1_introduccion.py", label="⬅️ Anterior: Introducción", icon="👈")
st.page_link("pages/3_condicionales.py", label="➡️ Siguiente: Condicionales", icon="👉")