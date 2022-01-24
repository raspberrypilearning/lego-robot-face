## Emotionale Reaktionen auf Objekte

Um das Projekt abzuschließen, kannst du das Robotergesicht verschiedene Ausdrücke anzeigen lassen, je nachdem, was die Kamera sieht.

![Code mit der Kameraansicht auf der linken Seite, die verschiedene Bilder zeigt, die vor die Kamera gehalten werden. Rechts reagiert das Robotergesicht auf die Bilder.](images/completed_project.gif)

--- task ---

Beginne mit dem Importieren der `Classifier` Klasse aus der Datei, die du zuvor verwendet hast, und mit der Funktion `sleep`.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 7
line_highlights:
---
from classifier import Classifier 
from time import sleep
--- /code ---

--- /task ---

--- task ---

Erstelle dann eine Liste von Objekten, die der Klassifikator erkennen kann. Du kannst den `Schwellwert` später anpassen, um den Klassifikator bei seiner Erkennung mehr oder weniger genau zu machen.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 31
line_highlights:
---

gesehenes = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)
--- /code ---

--- /task ---

--- task ---

Erstelle nun ein dictionary, das Objekte mit verschiedenen Emotionen verknüpft. Du kannst deine eigenen Objekte und Emotionen auswählen, je nachdem, was du um dich herum hast, oder welche Bilder, du dir ausgedruckt hast.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 33
line_highlights:
---

reaktionen = {"broccoli":"neutral","teapot":"neutral","snake":"boese","hotdog":"gluecklich"}
--- /code ---

--- /task ---

--- task ---

Schließlich kannst du eine Schleife erstellen, die alle zwei Sekundenum überprüft, was in der Liste `gesehenes` erkannt wurde, und dann den Gesichtsausdruck gemäß deinem dictionary `Reaktionen` anzeigt.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 61
line_highlights:
---
while True: 
    sleep(1) 
    if gesehenes.item != gesehenes.last_item: 
        bild = gesehenes.item 
        if bild in reaktionen.keys(): 
            gesicht_machen(gesichter[reaktionen[item]]) 
    sleep(1)
--- /code ---

--- /task ---

--- save ---
