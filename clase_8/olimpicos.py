import pandas as pd
import numpy as np

#ejercicio 1 Importar la base de datos athlete_events.csv , y reportar la cantidad de registros (filas) 
df = pd.read_csv('/Users/sariasc/Projects/python/classroom_exercises/python_classes_desafioltm/clase_8/athlete_events.csv')

ejercicio_1 = df.shape

ejercicio_2 = len(df["Games"].unique())

ejercicio_3 = df["Season"].value_counts('%')

ejercicio_4 = df[(df['Season'] == "Summer") & (df['Year'] == df["Year"].min())]["City"].unique()

df_winter = df[df['Season'] == "Winter"]
ejercicio_5 = df_winter[df_winter["Year"] == df_winter["Year"].min()]["City"].unique()

ejercicio_6 = df["NOC"].value_counts().sort_values(ascending = False).head(10)

ejercicio_7 = df["Medal"].value_counts('%')

ejercicio_8 = df[(df['Season'] == "Summer") & (df['Year'] == df["Year"].min())]["NOC"].unique()