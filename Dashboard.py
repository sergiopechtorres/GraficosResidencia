import pandas as pd
import plotly.express as px
import streamlit as st
  dff = pd.read

df = pd.read_excel(
    io='Data.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',



)

st.dataframe(df)
st.sidebar.header("Filtra aqui por favor:")
entidad= st.sidebar.multiselect(
    "Seleccionar la ENTIDAD FEDERATIVA",
    options=df["ENTIDAD_FEDERATIVA"].unique(),
    default=df["ENTIDAD_FEDERATIVA"].unique()
)

municipio = st.sidebar.multiselect(
    "Seleccionar el MUNICIPIO",
    options=df["MUNICIPIO"].unique(),
    default=df["MUNICIPIO"].unique()

)

institucion = st.sidebar.multiselect(
    "Seleccionar el municipio",
    options=df["INSTITUCIÓN DE EDUCACIÓN SUPERIOR"].unique(),
    default=df["INSTITUCIÓN DE EDUCACIÓN SUPERIOR"].unique()
)

df_selection = df.query(
    "ENTIDAD_FEDERATIVA == @entidad  "


)


st.dataframe(df_selection)