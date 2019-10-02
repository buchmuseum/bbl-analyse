# Skripte zur Analyse des Börsenblatts für den Deutschen Buchhandel 1834-1945

Über die OAI-Schnittstelle der Sächsischen Landesbibliothek SLUB werden die METS-Metadaten zu den Digitalisaten des Börsenblatts für den Deutschen Buchhandel heruntergeladen. Mit verschiedenen Skripten wurden diese Daten unterschiedlich ausgewertet.

Aus den Daten wird die Anzahl der Seiten pro Ausgabe ausgelesen und als csv gespeichert. Das Ergebnis wird mit Dash/Plotly als interaktives Diagramm dargestellt.

Ein anderes Skript lädt die ALTO-XML-Dateien, die den Volltext der digitalisierten Seiten enthalten und analysiert die Anzahl der erkannten Zeilen, um daraus Rückschlüsse auf den Inhalt der Seite zu ziehen.

## bbl-xml-grab.py
mets-daten über die OAI-Schnittstelle der SLUB laden, für jedes heft eine einzelne xml-datei anlegen
## bbl-mets-auswertung.py
wertet die heruntergeladenen daten aus und schreibt seitenliste.csv, die id eines jeden heftes und die zugehörige seitenzahl enthält
## bbl-dash.py
ein diagram der seitenzahlen mit dash erstellen
## analyse.py
einfache analysen über die seitenzahlen

## plot.py
Diagram mit bokeh erstellen, nicht weiterentwickelt, dash ist momentan die interessantere alternative
