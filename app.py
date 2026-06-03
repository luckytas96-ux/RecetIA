import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="RecetIA",
    layout="centered"
)

st.title("RecetIA")
st.subheader("Generador de recetas con Inteligencia Artificial")

st.write(
    "Ingresá los ingredientes que tenés disponibles y la aplicación generará "
    "una receta simple, económica y fácil de preparar."
)

# Verificar API Key
if "OPENAI_API_KEY" not in st.secrets:
    st.error("No se encontró la API Key de OpenAI en secrets.toml.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.header("Datos para generar la receta")

ingredientes = st.text_area(
    "Ingredientes disponibles:",
    placeholder="Ejemplo: arroz, pollo, cebolla, tomate"
)

tipo_comida = st.selectbox(
    "Tipo de comida:",
    ["Cualquiera", "Desayuno", "Almuerzo", "Merienda", "Cena"]
)

dificultad = st.selectbox(
    "Dificultad:",
    ["Fácil", "Media", "Avanzada"]
)

tiempo = st.selectbox(
    "Tiempo disponible:",
    ["Menos de 15 minutos", "Entre 15 y 30 minutos", "Más de 30 minutos"]
)

if st.button("Generar receta"):
    if ingredientes.strip() == "":
        st.warning("Por favor, ingresá al menos un ingrediente.")
    else:
        with st.spinner("Generando receta..."):
            prompt = f"""
Actuá como un chef profesional.

Generá una receta simple, clara y económica usando principalmente estos ingredientes:
{ingredientes}

Tipo de comida: {tipo_comida}
Dificultad: {dificultad}
Tiempo disponible: {tiempo}

La respuesta debe tener este formato:

Nombre de la receta:
Ingredientes:
Preparación paso a paso:
Tiempo estimado:
Consejos adicionales:

Evitá ingredientes difíciles de conseguir.
Si falta algún ingrediente básico, sugerí reemplazos simples.
"""

            respuesta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Sos un asistente experto en cocina práctica, económica y sencilla."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7
            )

            receta = respuesta.choices[0].message.content

            st.success("Receta generada con éxito.")
            st.markdown(receta)

st.header("Cómo funciona RecetIA")

st.write(
    """
1. El usuario ingresa los ingredientes disponibles.
2. Selecciona el tipo de comida, la dificultad y el tiempo.
3. Presiona el botón Generar receta.
4. La Inteligencia Artificial procesa la información.
5. La aplicación muestra una receta personalizada.
    """
)

st.header("Importancia de la aplicación")

st.write(
    """
RecetIA permite ahorrar tiempo, reducir el desperdicio de alimentos
y facilitar la organización diaria de las comidas mediante el uso de
Inteligencia Artificial.
    """
)

st.markdown("---")
st.caption("Proyecto Final - RecetIA")