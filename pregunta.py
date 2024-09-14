"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Cargar el dataset
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    
    # Eliminar filas duplicadas
    df.drop_duplicates(inplace=True)
    
    # Eliminar filas con datos faltantes
    df.dropna(inplace=True)

    # Normalización de los textos
    # Convertir todo a minúsculas, eliminar espacios en blanco al inicio y final
    df["sexo"] = df["sexo"].str.lower().str.strip()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip().str.replace('_', ' ').str.replace('-', ' ')
    df["barrio"] = df["barrio"].str.lower().str.strip().str.replace('_', ' ').str.replace('-', ' ')
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip().str.replace('_', ' ').str.replace('-', ' ')

    # Normalización de las fechas
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], errors='coerce')
    
    # Eliminar filas con fechas inválidas
    df = df.dropna(subset=["fecha_de_beneficio"])
    
    return df
