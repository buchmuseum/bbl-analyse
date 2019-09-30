import requests
from bs4 import BeautifulSoup as soup
import math
import concurrent.futures
import re
import time

start = time.perf_counter()


base_url = 'https://digital.slub-dresden.de/oai/'
recordsearch_term = {'verb': 'GetRecord', 'metadataPrefix': 'mets'}
#listsearch_term = {'verb': 'ListIdentifiers', 'metadataPrefix': 'mets', 'set': 'ldp-boersenblatt'}
listsearch_term = {'verb': 'ListIdentifiers', 'metadataPrefix': 'mets', 'set': 'becher-institute-exam-paper'}

def download_xml(params):
    response = requests.get(base_url, params=params)
    output_soup = soup(response.content, "lxml")
    return output_soup

def download_record(id):
    output_soup = download_xml({'verb': 'GetRecord', 'metadataPrefix': 'mets', 'identifier': id})
        
    #slub_id = output_soup.find("slub:id").get_text().strip()
    #slub_id = re.search('\d{8}X.+',id).group()
    slub_id = re.search('id-.+',id).group()
    with open(f'./test/{slub_id}.mets', mode='w', encoding='utf-8') as f:
        f.write(output_soup.prettify())

#erstanfrage um zu ermitteln, wieviele ergebnisse die suche im ganzen hat
xml_soup = download_xml(listsearch_term)

suchlaeufe = math.ceil(int(xml_soup.resumptiontoken['completelistsize']) // 25) + 1
print(suchlaeufe, 'Suchläufe')

for i in range(suchlaeufe):
    xml_soup_new = download_xml(listsearch_term) if i == 0 else download_xml({'verb': 'ListIdentifiers','resumptionToken': resumption_token})

    id_liste = [id.get_text().strip() for id in xml_soup_new.find_all('identifier')]
    #threads über diese liste laufen lassen

    with concurrent.futures.ThreaPoolExecutor() as executor:
        results = executor.map(download_record, id_liste)

    new_token = xml_soup_new.find('resumptiontoken').get_text()
    print('neuer cursor ', xml_soup_new.resumptiontoken['cursor'])
 
    resumption_token = new_token
    print ('neuer token=', resumption_token)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')