import pandas as pd
import numpy as np
#no funcionó colocando el archivo en el mismo directorio, igual debo colocar ruta completa.
df = pd.read_csv("/Users/sariasc/Projects/python/classroom_exercises/python_classes_desafioltm/clase_8/nations.csv")

#print(df.shape)

#print(df.head)

df = df.drop(columns = "Unnamed: 0")

#print(df.head(2))

print(df["region"])
print(df["region"].value_counts() / len(df))
print(df["region"].value_counts().mean())