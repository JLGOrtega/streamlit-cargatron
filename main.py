import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="My streamlit project",
    page_icon="👒",
    layout="wide")


option = st.sidebar.selectbox(
    'Selecciona la vista: ',
    ('Home', 'Visualizaciones', 'Mapa'),
    index=0)




datos = pd.read_csv("data/red_recarga_acceso_publico_2021.csv", sep=";")

uploaded_file = st.sidebar.file_uploader("Elige un csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)


st.title("CARGATRON APP")

if option == "Home":

    st.subheader("Home")

    with st.expander("Detalles de la aplicacion - Haz click para expandir"):
        st.write("""
        Esto es una aplicacion bla
        1. Vamos a crear un selector (st.selectbox)
        2. Para que el selector se vea siempre y así poder cambiar de página lo vamos a tener
        en el lateral (st.sidebar)
        3. Vamos a separar los elementos que van a home y los que van a los datos en
        distintas funciones
        4. Vamos a crear una estructura para que dependiendo de la selección del menu
        podamos ver la pagina de home o la de los datos
        """)
        
        st.image("https://i.insider.com/5dd70496fd9db226981ff4e2?width=1000&format=jpeg", width=600,
                        caption="Ahi un astronauta to fresco!")

  

    with st.echo():
        st.write(datos)
    with st.echo():
        # Codigo para generar numeros pares
        lista = list(range(10))
        even_list = [x for x in lista if x%2==0]
        st.write(even_list)


elif option == "Mapa":
    st.subheader("Mapa")
    datos_pal_mapa = datos[["latidtud", "longitud"]]    
    datos_pal_mapa.columns = ["lat", "lon"]

    st.subheader("Mapa Cargadores: ")
    st.map(datos_pal_mapa)
elif option == "Visualizaciones":
    st.subheader("VIZ")
    datos_pal_barchart = datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    st.subheader("Numero de cargadores por distrito")
    st.bar_chart(datos_pal_barchart, x="DISTRITO", y="Nº CARGADORES")
