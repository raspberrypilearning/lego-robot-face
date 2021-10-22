## Den Mund motorisieren

--- task ---

Öffnen Sie **Thonny** aus dem Programmiermenü und speichern Sie eine neue Datei namens `robot_face.py`, und stellen Sie sicher, dass Sie sie im selben Verzeichnis wie `classifier.py`, `labels.txt`und die 8×8-Pixel-Kunst speichern Bilder.

![Dateistruktur, die anzeigt, wo robot_face.py gespeichert werden soll.](images/file_structure.png)

--- /task ---

--- task ---

Fügen Sie zunächst den Import hinzu, den Sie zum Steuern der LEGO® Technic™-Motoren benötigen.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights:
---
from buildhat import Motor --- /code ---

--- /task ---

--- task ---

Erstellen Sie zwei neue Objekte für den linken und rechten Motor. In diesem Beispiel wird der rechte Motor an Port A und der linke an Port B angeschlossen.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

Mund_r = Motor('A') Mund_l = Motor('B') --- /Code ---

--- /task ---

--- task ---

Beide Motoren sollten beim Programmstart `0`

--- code ---
---
language: python filename: robot_face,py line_numbers: true line_number_start: 5
line_highlights:
---

mund_r.run_to_position(0) mund_l.run_to_position(0) --- /code ---

--- /task ---

--- task ---

Erstellen Sie eine Funktion, die die Mundmotoren bewegt. Sie müssen sich in entgegengesetzte Richtungen drehen, sodass der linke Motor auf einen negativen Wert und der rechte Motor auf einen positiven Wert dreht. Durch Hinzufügen von `Blocking = False` drehen sich beide Motoren gleichzeitig.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 8
line_highlights:
---
def move_mouth (Position, Geschwindigkeit = 100): mouth_l.run_to_position (Position * -1, Geschwindigkeit, Sperrung = False) #Turn negative Position mouth_r.run_to_position (Position, Geschwindigkeit, Sperrung = False) #Turn auf positive Position --- /code ---

--- /task ---

--- task ---

Führen Sie Ihr Programm aus und testen Sie dann Ihre neue Funktion in der **Shell**.

--- code ---
---
Sprache: Python Dateiname: Zeilennummer: false Zeilennummer_Start:
line_highlights:
---
> > > move_mouth(45) move_mouth(0) --- /code ---

Wenn sich Ihre Motoren in die falsche Richtung bewegen, versuchen Sie, ihre Ports zu wechseln.

--- /task ---

--- save ---
