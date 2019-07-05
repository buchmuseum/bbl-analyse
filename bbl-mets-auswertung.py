from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
import os
import re

gesamtseiten = 0
liste = {}

for file in os.listdir("./data/"):
    seiten = 0
    if file.endswith(".mets"):
        with open('./data/' + file) as fp:
            xml_soup = soup(fp, "xml")
    slub_id = re.sub(r'\n   oai:de:slub-dresden:db:id-|\n  ','',xml_soup.identifier.string)
    seiten = len(xml_soup.find_all("mets:div", TYPE='page'))
    liste.update({slub_id:seiten})
    gesamtseiten = gesamtseiten + seiten
    print(gesamtseiten)

df = pd.DataFrame.from_dict(liste,orient='index',columns=['seiten'])

df.to_csv("./seitenliste.csv", sep=',')

""" df['slub_id'][:3].astype(str)

df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
df.slub_id = df.slub_id.astype(str)
df.slub_id = df.slub_id.str[:4] + '-' + df.slub_id.str[4:6] + '-' + df.slub_id.str[6:8] 

df.slub_id = df.slub_id.str[-8:-4] + '-' + df.slub_id.str[-4:-2]  + '-' + df.slub_id.str[-2:]
"""

