from bs4 import BeautifulSoup as soup
import pandas as pd
import os
import re
import concurrent.futures
import time

start = time.perf_counter()

liste = {}


def mets_analyse(filename):
    seiten = 0
    with open(f'daten/{filename}', 'rb') as fp:
        xml_soup = soup(fp, "lxml")
    slub_id = re.search('\d+X-\d+', xml_soup.find('identifier').get_text()).group() if xml_soup.find('identifier') else None
    seiten = len(xml_soup.find_all("mets:div", {'type': 'page'})) if xml_soup.find_all("mets:div", {'type': 'page'}) else 0
    return slub_id, seiten


dateiliste = os.listdir('./daten')

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(mets_analyse, dateiliste)

    for slub_id, seiten in results:
        liste.update({slub_id: seiten})


df = pd.DataFrame.from_dict(liste, orient='index', columns=['seiten'])

print(df)

# df.slub_id = f'{df.slub_id.str[:4]}-{df.slub_id.str[4:6]}-{df.slub_id.str[6:8]}'


df.to_csv("./seitenliste.csv", sep=',')


# df['slub-id'][:3].astype(str)

# df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
# df.slub_id = df.slub_id.astype(str)
# df.slub_id = df.slub_id.str[:4] + '-' + df.slub_id.str[4:6] + '-' + df.slub_id.str[6:8]

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
