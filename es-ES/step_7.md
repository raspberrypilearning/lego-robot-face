## Motoriza la boca

--- task ---

Abre **Thonny** desde el menú de programación y guarda un nuevo archivo llamado `robot_face.py`, y asegúrate de guardarlo en el mismo directorio que `classifier.py`, `labels.txt` y las imágenes pixel art de 8 × 8.

![Estructura de archivo que muestra dónde debe almacenarse robot_face.py.](images/file_structure.png)

--- /task ---

--- task ---

Comienza agregando la importación que necesitarás para controlar los motores LEGO® Technic ™.

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

Crea dos nuevos objetos para los motores izquierdo y derecho. En este ejemplo, el motor derecho está conectado al puerto A y el izquierdo al puerto B.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

boca_d = Motor ('A') 
boca_i = Motor ('B')
--- /code ---

--- /task ---

--- task ---

Ambos motores deben arrancar en la posición `0` cuando se inicia el programa.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 5
line_highlights:
---

boca_d.run_to_position(0) 
boca_i.run_to_position(0)
--- /code ---

--- /task ---

--- task ---

Crea una función que mueva los motores de la boca. Deben girar en direcciones opuestas, por lo que el motor izquierdo cambiará a un valor negativo y el motor derecho a un valor positivo. Agregar `blocking=False` hará que ambos motores giren al mismo tiempo.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 8
line_highlights:
---
def mover_boca (posicion, velocidad = 100): 
    boca_i.run_to_position (posicion * -1, velocidad, blocking=False) # Gira a la posición negativa 
    boca_d.run_to_position (posicion, velocidad, blocking=False) # Gira a la posición positiva
--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa y luego prueba tu nueva función en la **Consola**.

--- code ---
---
language: python 
filename: 
line_numbers: false 
line_number_start:
line_highlights:
---
>>> mover_boca(45) 
>>> mover_boca(0)
--- /code ---

Si tus motores se mueven en la dirección incorrecta, intenta cambiar los puertos.

--- /task ---

--- save ---
