## Programa los ojos

Las matrices LED pueden mostrar imágenes de 8 × 8 píxeles en sus pantallas. Estos se pueden utilizar para mostrar diferentes movimientos de los ojos.

--- task ---

Agrega tres bibliotecas nuevas que te permitan mostrar imágenes en las pantallas LED.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start:
line_highlights: 2-4
---
from buildhat import Motor 
import board 
from adafruit_ht16k33.matrix import Matrix8x8 
from PIL import Image

--- /code ---

--- /task ---

--- task ---

Configura objetos para usar el ojo izquierdo y derecho. Por ahora, las imágenes en cada ojo serán las mismas, pero puedes ajustar tu código más tarde, si deseas usar diferentes imágenes en las diferentes pantallas, dependiendo de en cuál soldaste las almohadillas `A0`.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 13
line_highlights:
---

i2c = board.I2C() 
ojo_izquierdo = Matrix8x8(i2c, address=0x70) 
ojo_derecho = Matrix8x8(i2c, address=0x71)
--- /code ---

--- /task ---

--- task ---

Usando la biblioteca PIL, algunas de las imágenes se pueden abrir y almacenar.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 17
line_highlights:
---

neutral = Image.open("neutral.png").rotate(90) 
abierto = Image.open("wide.png").rotate(90) 
enojado = Image.open("angry.png").rotate(90) 
abajo = Image.open("look_down.png").rotate(90)
--- /code ---

--- /task ---

--- task ---

Escribe una nueva función para cambiar los ojos que se muestran en los LED.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 38
line_highlights:
---
def cambiar_ojos(izquierda,derecha): 
    ojo_izquierdo.image(izquierda) 
    ojo_derecho.image(derecha)
--- /code ---

--- /task ---

--- task ---

Ejecuta tu código y luego usa la **Consola** para probar tu nueva función.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start:
line_highlights:
---
>>> cambiar_ojos(neutral, neutral) 
>>> cambiar_ojos(abierto, abierto) 
>>> cambiar_ojos(enojado, enojado)
--- /code ---

--- /task ---

No dudes en utilizar las demás imágenes disponibles o crear las tuyas propias e incluirlas en el proyecto.

--- save ---
