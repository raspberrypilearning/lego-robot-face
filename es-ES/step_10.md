## Cambiando caras

Ahora es el momento de unir todas sus diferentes funciones para cambiar todo el rostro.

--- task ---

Para empezar, debe crear un diccionario para almacenar las diferentes expresiones faciales que desea utilizar. Esto dará valores para los motores de la boca, el motor de las cejas y los ojos.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

caras = { "neutral": {"boca": 0, "ojo_derecho": neutral, "ojo_izquierdo": neutral, "cejas": 0}, "feliz": {"boca": 45, "ojo_derecho": wide, "left_eye": wide, "eyebrows": 150}, "angry": {"mouth": - 20, "right_eye": enojado, "left_eye": enojado, "eyebrows": - 150}, " triste ": {" boca ": - 45," ojo_derecho ": mirar_abajo," ojo_izquierdo ": mirar_abajo," cejas ": - 40} } --- / código ---

--- /task ---

--- task ---

Ahora cree una función que fijará la boca, las cejas y los ojos.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (cara): change_eyes (cara ["right_eye"], cara ["left_eye"]) move_mouth (cara ["boca"]) move_eyebrows (cara ["cejas"]) --- / código - -

--- /task ---

--- task ---

Ejecute su código y luego use **Shell** para probar su nueva función.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face (caras ['enojado']) set_face (caras ['feliz']) set_face (caras ['neutral']) set_face (caras ['triste']) --- / código ---

--- /task ---

--- save ---
