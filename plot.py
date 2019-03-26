import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file

df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
df.ausgabe = pd.to_datetime(df.ausgabe)

output_file = "plot.html"

p = figure(title="Seitenverteilung Bbl", x_axis_label='Ausgabe', x_axis_type="datetime", y_axis_label='Seiten', plot_width=1500, plot_height=800)
p.vbar(x=df['ausgabe'], bottom=0, top=df['seiten'], width=0.1)


show(p)