## Den Mund motorisieren

--- task ---

Öffne **Thonny** aus dem Entwicklungsmenü und speichere eine neue Datei namens `robot_face.py`. Achte darauf, dass Sie im selben Verzeichnis wie `classifier.py`, `labels.txt`und die 8×8-Pixel-Kunst Bilder gespeichert wird.

![Dateistruktur, die anzeigt, wo robot_face.py gespeichert werden soll.](images/file_structure.png)

--- /task ---

--- task ---

Füge zunächst den Import hinzu, den du zum Steuern der LEGO® Technic™-Motoren benötigst.

--- code ---
---
language: python
filename: robot_face.py
line_numbers: true
line_number_start: 
line_highlights:
---
from buildhat import Motor
--- /code ---

--- /task ---

--- task ---

Erstelle zwei neue Objekte für den linken und rechten Motor. In diesem Beispiel wird der rechte Motor an Port A und der linke an Port B angeschlossen.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

mund_r = Motor('A') 
mund_l = Motor('B')

--- /code ---

--- /task ---

--- task ---

Beide Motoren sollten beim Programmstart in der `0` Position starten.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 5
line_highlights:
---

mund_r.run_to_position(0) 
mund_l.run_to_position(0)
--- /code ---

--- /task ---

--- task ---

Erstelle eine Funktion, die die Mundmotoren bewegt. Sie müssen sich in entgegengesetzte Richtungen drehen, sodass der linke Motor auf einen negativen Wert und der rechte Motor auf einen positiven Wert dreht. Durch Hinzufügen von `blocking = False` drehen sich beide Motoren gleichzeitig.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 8
line_highlights:
---
def mund_bewegen (position, geschwindigkeit = 100): 
    mund_l.run_to_position (position * -1, geschwindigkeit, blocking = False) #drehe zur negativen Position 
    mund_r.run_to_position (position, geschwindigkeit, blocking = False) #drehe zur positiven Position
--- /code ---

--- /task ---

--- task ---

Führe Ihr Programm aus und teste dann deine neue Funktion in der **Shell**.

--- code ---
---
language: python 
filename: 
line_numbers: false 
line_number_start:
line_highlights:
---
> > > mund_bewegen(45) 
> > > mund_bewegen(0)
--- /code ---

Wenn sich deine Motoren in die falsche Richtung bewegen, versuche ihre Ports zu wechseln.

--- /task ---

--- save ---
