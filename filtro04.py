# Importar las librerias correspondientes de Pandas y etc.
from operator import index
import numpy as np
import pandas as pd
# Para importar las Listas de Areas por carrera del archivo FiltroAreas.py
from FiltroAreas import FiltroAreasComputacional, FiltroAreasSoftware, FiltroAreasInformatica, FiltroAreasInteligencia, FiltroAreasOtros
from FiltroAreas import FiltroAreasSistemasCom, FiltroAreasSistemasInf, FiltroAreasTecnologias, FiltroAreasTecDeLaInformacion, FiltroAreasTelematica

df = pd.read_excel('Data.xlsx')

conditionlist = [
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasComputacional))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasSoftware))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasInformatica))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasInteligencia))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasOtros))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasSistemasCom))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasSistemasInf))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasTecnologias))),
    (df['PROGRAMADEESTUDIOS'].str.contains(
        '|'.join(FiltroAreasTecDeLaInformacion))),
    (df['PROGRAMADEESTUDIOS'].str.contains('|'.join(FiltroAreasTelematica))),


]
choicelist = ['CIENCIAS COMPUTACIONALES', 'DESARROLLO DE SOFTWARE', 'INFORMÁTICA', 'INTELIGENCIA ARTIFICIAL', 'OTROS',
              'SISTEMAS COMPUTACIONALES', 'SISTEMAS DE INFORMACIÓN', 'TECNOLOGÍAS DE INFORMACIÓN', 'TECNOLOGIAS DE LA INFORMACIÓN', 'TELEMÁTICA']
clasificacion = df['Carrera Areas'] = np.select(
    conditionlist, choicelist, default='No especificado')

df.to_excel("Data.xlsx", index=False)
print(df)
