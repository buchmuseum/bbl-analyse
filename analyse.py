import pandas as pd
import numpy as np

df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
df.ausgabe = pd.to_datetime(df.ausgabe)

max_seiten = df[df.seiten==df.seiten.max()]

print ("Ausgabe mit den meisten Seiten erschien am", max_seiten.iloc[0,0], "mit", max_seiten.iloc[0,1], "Seiten.")