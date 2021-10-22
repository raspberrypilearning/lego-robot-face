## Gesichter ändern

Jetzt ist es an der Zeit, all Ihre verschiedenen Funktionen zusammenzubringen, um das gesamte Gesicht zu verändern.

--- task ---

Zunächst müssen Sie ein Wörterbuch erstellen, um die verschiedenen Gesichtsausdrücke zu speichern, die Sie verwenden möchten. Dies ergibt Werte für die Mundmotoren, den Augenbrauenmotor und die Augen.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

Gesichter = { "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0}, "happy":{"mouth":45, "right_eye": breit, "left_eye":wide, "eyebrows":150}, "wütend":{"mouth":-20, "right_eye":wütend, "left_eye":wütend, "eyebrows":-150}, " traurig":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

Erstellen Sie nun eine Funktion, die Mund, Augenbrauen und Augen festlegt.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (face): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code - --

--- /task ---

--- task ---

Führen Sie Ihren Code aus und verwenden Sie dann die **Shell** , um Ihre neue Funktion zu testen.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['angry']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
