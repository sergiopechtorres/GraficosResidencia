# Importar las librerias correspondientes de Pandas,Openpyxl y etc.
import pandas as pd
# Para importar las Listas del archivo FiltroAreas.py
from FiltroAreas import FiltroOTROS, FiltroPOLITECNICA, FiltroUNIVERSIDAD, searchfor, FiltroTECNOLOGIA
from FiltroAreas import FiltroTECNM

# Abrir el archivo EjemploMain con la variable df
df = pd.read_excel('filtro02.xlsx')


# Filtrar por Areas
filtro = df[df.PROGRAMADEESTUDIOS.str.contains('|'.join(searchfor))]
# Imprimir el primer resultado
print(filtro)
filtro.to_excel("Filtro03.xlsx", index=False)

