import pandas as pd
import numpy as np

def extraerdatos():
    df = pd.read_csv('./appstore_games.csv', encoding='latin')
    df.columns = df.columns.to_series().apply(lambda x: x.strip())
    df.isnull().sum().sort_values().head()/17007
    df_reducido=df[["Name","User Rating Count","Price","Languages","Primary Genre",'Developer',]]
    return df_reducido

datos= extraerdatos()
