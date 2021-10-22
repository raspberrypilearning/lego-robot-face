## Augenbrauen programmieren

Der dritte Motor wird verwendet, um die Augenbrauen des Gesichts zu bewegen.

--- task ---

Richten Sie ein Objekt für den Motor der Augenbrauen ein.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 3
line_highlights: 5
---
Mund_r = Motor('A') Mund_l = Motor('B') Augenbrauen = Motor('C')

--- /code ---

--- /task ---

--- task ---

Stellen Sie sicher, dass Ihr großer Motor so positioniert ist, dass der **Lollipop** und der **Kreis** ausgerichtet sind und dass die Augenbrauen Ihres Gesichts horizontal ausgerichtet sind. Wenn dies nicht der Fall ist, müssen Sie Ihren Build möglicherweise ein wenig anpassen.

![Motor so gedreht, dass Lutscher und Kreis ausgerichtet sind.](images/motor_0.jpg)

![Das Robotergesicht mit den Augenbrauen in einer horizontalen Position.](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

Stellen Sie nun den Motor so ein, dass er sich `0`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights: 9
---
mund_r.run_to_position(0) mund_l.run_to_position(0) eyebrows.run_to_position(0) --- /code ---

--- /task ---

Es gibt drei Augenbrauenpositionen, die hier angezeigt werden, aber Sie können mehr erstellen.

- `0` die Augenbrauen horizontal erscheinen
- `150` senkt die Augenbrauen
- `-150` hebt die Augenbrauen


--- task ---

Fügen Sie eine Funktion hinzu, die die aktuelle Augenbrauenposition erhält, und wenn die Position, an die sie sich bewegen soll, kleiner als die aktuelle ist, bewegt sie sich gegen den Uhrzeigersinn, andernfalls bewegt sie sich im Uhrzeigersinn.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---
def move_eyebrows (position): current_position = if position < current_position: rotation = 'entgegen dem Uhrzeigersinn' else: rotation = 'im Uhrzeigersinn' eyebrows.run_to_position(position, direction = rotation)

--- /code ---

--- /task ---

--- task ---

Führen Sie Ihren Code aus und testen Sie Ihre neue Funktion in der **Shell**.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights:
---
> > > move_eyebrows(-150) move_eyebrows(150) move_eyebrows(0) --- /code ---

--- /task ---

--- save ---
