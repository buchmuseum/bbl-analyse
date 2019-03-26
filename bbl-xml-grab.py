from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

base_url = "http://digital.slub-dresden.de/oai/?verb=ListRecords&metadataPrefix=mets&set=ldp-boersenblatt"
weiter = False

#erstanfrage
oia_raw = uReq(base_url)
suche_xml = oia_raw.read()
oia_raw.close()
xml_soup = soup(suche_xml, "xml")

#ergebnisse der ersten suche werden in output-file geschrieben
for record in xml_soup.find_all("record"):
    slub_id = record.find("slub:id").string
    with open("./" + slub_id + ".mets", mode='a+') as file:
        file.write(record.prettify())
  
resumption_token = xml_soup.find('resumptionToken').string

if resumption_token:
    weiter = True

while weiter == True:
    oia_raw = uReq("http://digital.slub-dresden.de/oai/?verb=ListRecords&resumptionToken=" + resumption_token)
    suche_xml = oia_raw.read()
    oia_raw.close()
    xml_soup_new = soup(suche_xml, "xml")

    new_token = xml_soup_new.find('resumptionToken').string

    if new_token:
        weiter = True
    else:
        weiter = False

    cursor = int(xml_soup_new.resumptionToken['cursor'])
    print (cursor)    

    for record in xml_soup_new.find_all("record"):
        slub_id = record.find("slub:id").string
        with open("./" + slub_id + ".mets", mode='a+') as file:
            file.write(record.prettify())
 
    resumption_token = new_token
    print (resumption_token)








#complete_list_size = int(xml_soup.resumptionToken['completeListSize'])
#cursor = int(xml_soup.resumptionToken['cursor'])



# for record in xml_soup.ListRecords:
#     seiten = len(record.find("mets:fileGrp", USE='MIN'))
#     slub_id = record.find("slub:id", limit=1).string






# ######
# record.metadata.mets:mets.mets:fileSec.mets:fileGrp USE="MIN".mets:file
# return len(soup.find_all(tag_name))