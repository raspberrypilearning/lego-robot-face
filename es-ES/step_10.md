## Cambiando caras

Ahora es el momento de unir todas sus diferentes funciones para cambiar las caras.

--- task ---

Para empezar, debes crear un diccionario para almacenar las diferentes expresiones faciales que deseas utilizar. Esto dará valores para los motores de la boca, el motor de las cejas y los ojos.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

caras = { "neutral": {"boca": 0, "ojo_derecho": neutral, "ojo_izquierdo": neutral, "cejas": 0}, "feliz": {"boca": 45, "ojo_derecho": abierto, "left_eye": abierto, "cejas": 150}, "enojado": {"boca": - 20, "ojo_derecho": enojado, "ojo_izquierdo": enojado, "cejas": - 150}, " triste ": {" boca ": - 45," ojo_derecho ": mirar_abajo," ojo_izquierdo ": mirar_abajo," cejas ": - 40} } --- /code---

--- /task ---

--- task ---

Ahora crea una función que fijará la boca, las cejas y los ojos.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def fijar_cara(cara): cambiar_ojos (cara ["ojo_derecho"], cara ["ojo_izquierdo"]) mover_boca(cara ["boca"]) mocer_cejas (cara ["cejas"]) --- /code- -

--- /task ---

--- task ---

Ejecuta tu código y luego usa la **Consola** para probar tu nueva función.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > fijar_cara(caras ['enojado']) fijar_cara(caras ['feliz']) fijar_cara(caras ['neutral']) fijar_cara(caras ['triste']) --- /code ---

--- /task ---

--- save ---
