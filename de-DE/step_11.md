## Emotionale Reaktionen auf Objekte

Um das Projekt abzuschließen, können Sie das Robotergesicht verschiedene Ausdrücke anzeigen lassen, je nachdem, was die Kamera sehen kann.

![Code auf der linken Seite mit der Kameraansicht, die verschiedene Bilder zeigt, die vor der Kamera gehalten werden. Rechts reagiert das Robotergesicht auf die Bilder.](images/completed_project.gif)

--- task ---

Beginnen Sie mit dem Importieren der `Classifier` aus der Datei, die Sie zuvor verwendet haben, zusammen mit der Funktion `sleep`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
aus Klassifikator importieren Klassifikator aus Zeitimport Schlaf --- /code ---

--- /task ---

--- task ---

Erstellen Sie dann eine Liste von Objekten, die der Klassifikator erkennen kann. Sie können die `Schwelle` später anpassen, um den Klassifikator bei seiner Erkennung mehr oder weniger genau zu machen.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5) --- /code ---

--- /task ---

--- task ---

Erstellen Sie nun ein Wörterbuch, das Objekte mit verschiedenen Emotionen verknüpft. Sie können Ihre eigenen Objekte und Emotionen auswählen, je nachdem, was Sie um sich herum haben, oder Bilder, die Sie ausgedruckt haben.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

Reaktionen = {"broccoli":"neutral","teapot":"neutral","snake":"w\u00fcrrend","hotdog":"froh"} --- /code ---

--- /task ---

--- task ---

Schließlich können Sie alle zwei Sekunden eine Schleife erstellen, um zu überprüfen, was in der `seen_items` , und dann den Gesichtsausdruck gemäß Ihrem `Reaktionen` Wörterbuch anzeigen.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep(1) if seen_items.item != seen_items.last_item: item = seen_items.item wenn item in set_face(faces[reactions[item]]) sleep(1) --- /code ---

--- /task ---

--- save ---
