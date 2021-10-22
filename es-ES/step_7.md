## Motorizar la boca

--- task ---

Abra **Thonny** desde el menú de programación y guarde un nuevo archivo llamado `robot_face.py`, y asegúrese de guardarlo en el mismo directorio que `classifier.py`, `labels.txt`y el pixel art de 8 × 8 imágenes.

![Estructura de archivo que muestra dónde debe almacenarse robot_face.py.](images/file_structure.png)

--- /task ---

--- task ---

Comience agregando la importación que necesitará para controlar los motores LEGO® Technic ™.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights:
---
from buildhat import Motor --- /code ---

--- /task ---

--- task ---

Crea dos nuevos objetos para los motores izquierdo y derecho. En este ejemplo, el motor derecho está conectado al puerto A y el izquierdo al puerto B.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

boca_r = Motor ('A') boca_l = Motor ('B') --- / código ---

--- /task ---

--- task ---

Ambos motores deben arrancar en la posición `0` cuando se inicia el programa.

--- code ---
---
language: python filename: robot_face,py line_numbers: true line_number_start: 5
line_highlights:
---

mouth_r.run_to_position (0) mouth_l.run_to_position (0) --- / código ---

--- /task ---

--- task ---

Crea una función que mueva los motores de la boca. Deben girar en direcciones opuestas, por lo que el motor izquierdo cambiará a un valor negativo y el motor derecho a un valor positivo. Agregar `= Falso` hará que ambos motores giren al mismo tiempo.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 8
line_highlights:
---
def move_mouth (posición, velocidad = 100): mouth_l.run_to_position (posición * -1, velocidad, bloqueo = Falso) # Gire a la posición negativa mouth_r.run_to_position (posición, velocidad, bloqueo = Falso) # Gire a la posición positiva --- / código ---

--- /task ---

--- task ---

Ejecute su programa y luego pruebe su nueva función en **Shell**.

--- code ---
---
idioma: python nombre de archivo: números de línea: falso inicio:
line_highlights:
---
> > > move_mouth (45) mover boca (0) --- / código ---

Si sus motores se mueven en la dirección incorrecta, intente cambiar sus puertos.

--- /task ---

--- save ---
