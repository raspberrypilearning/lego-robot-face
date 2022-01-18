## Programmierung der Augenbrauen

Der dritte Motor wird verwendet, um die Augenbrauen des Gesichts zu bewegen.

--- task ---

Richte ein Objekt für den Motor der Augenbrauen ein.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 3
line_highlights: 5
---
mund_r = Motor('A') 
mund_l = Motor('B') 
augenbrauen = Motor('C')

--- /code ---

--- /task ---

--- task ---

Stelle sicher, dass dein großer Motor so positioniert ist, dass der **Lollipop** und der **Kreis** ausgerichtet sind und dass die Augenbrauen deines Gesichts horizontal ausgerichtet sind. Wenn dies nicht der Fall ist, musst du deinen Aufbau möglicherweise ein wenig anpassen.

![Motor so gedreht, dass Lutscher und Kreis ausgerichtet sind.](images/motor_0.jpg)

![Das Robotergesicht mit den Augenbrauen in einer horizontalen Position.](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

Stelle nun den Motor so ein, dass er sich in die `0` Position dreht, wenn das Programm startet.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 7
line_highlights: 9
---
mund_r.run_to_position(0) 
mund_l.run_to_position(0) 
augenbrauen.run_to_position(0)
--- /code ---

--- /task ---

Es gibt drei Augenbrauenpositionen, die hier angezeigt werden, aber du kannst mehr erstellen.

- `0` lässt die Augenbrauen horizontal erscheinen
- `150` senkt die Augenbrauen
- `-150` hebt die Augenbrauen


--- task ---

Füge eine Funktion hinzu, die die aktuelle Augenbrauenposition erhält, und wenn die Position, an die sie sich bewegen soll, kleiner als die aktuelle ist eine Drehung gegen den Uhrzeigersinn ausführt, andernfalls eine Drehung im Uhrzeigersinn.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 17
line_highlights:
---
def augenbrauen_bewegen (position): 
    position_jetzt = augenbrauen.get_aposition() 
    if position < position_jetzt: 
        rotation = 'anticlockwise' 
    else: 
        rotation = 'clockwise' 
    augenbrauen.run_to_position(position, direction = rotation)

--- /code ---

--- /task ---

--- task ---

Führe Ihren Code aus und teste deine neue Funktion in der **Shell**.

--- code ---
---
language: python 
filename: 
line_numbers: false 
line_number_start:
line_highlights:
---
> > > augenbrauen_bewegen(-150) 
> > > augenbrauen_bewegen(150) 
> > > augenbrauen_bewegen(0)
--- /code ---

--- /task ---

--- save ---
