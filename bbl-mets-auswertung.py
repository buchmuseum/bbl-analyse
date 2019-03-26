from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
import os
import re


liste = {}

for file in os.listdir("."):
    seiten = 0
    if file.endswith(".mets"):
        with open(file) as fp:
            xml_soup = soup(fp, "xml")
    print (file)
    slub_id = xml_soup.identifier.string
    slub_id = re.sub(r'\n   oai:de:slub-dresden:db:id-','',slub_id)
    slub_id = re.sub(r'\n  ','',slub_id)
    if xml_soup.find_all("mets:div", TYPE='page'):
        seiten = len(xml_soup.find_all("mets:div", TYPE='page'))
    else:
        seiten = 0
    liste.update({slub_id:seiten})

df = pd.DataFrame.from_dict(liste,orient='index',columns=['seiten'])

df.to_csv("./seitenliste.csv", sep=',')


df['slub-id'][:3].astype(str)

df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
df.slub_id = df.slub_id.astype(str)
df.slub_id = df.slub_id.str[:4] + '-' + df.slub_id.str[4:6] + '-' + df.slub_id.str[6:8]

