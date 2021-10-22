## Programa los ojos

Las matrices LED pueden mostrar imágenes de 8 × 8 píxeles en sus pantallas. Estos se pueden utilizar para mostrar diferentes movimientos de los ojos.

--- task ---

Agregue tres bibliotecas nuevas que le permitan mostrar imágenes en las pantallas LED.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
de buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

Configure objetos para usar el ojo izquierdo y derecho. Por ahora, las imágenes en cada ojo serán las mismas, pero puede ajustar su código más tarde, si desea usar diferentes imágenes en las diferentes pantallas, dependiendo de en cuál soldara las almohadillas `A0`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = placa.I2C () ojo_izquierdo = Matrix8x8 (i2c, dirección = 0x70) ojo_derecha = Matrix8x8 (i2c, dirección = 0x71) --- / código ---

--- /task ---

--- task ---

Usando la biblioteca PIL, algunas de las imágenes se pueden abrir y almacenar.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

neutral = Image.open ("neutral.png"). rotate (90) wide = Image.open ("wide.png"). rotate (90) angry = Image.open ("angry.png"). rotate (90) look_down = Image.open ("look_down.png"). Rotate (90) --- / código ---

--- /task ---

--- task ---

Escribe una nueva función para cambiar los ojos que se muestran en los LED.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes (izquierda, derecha): left_eye.image (izquierda) right_eye.image (derecha) --- / código ---

--- /task ---

--- task ---

Ejecute su código y luego use **Shell** para probar su nueva función.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes (neutral, neutral) change_eyes (ancho, ancho) change_eyes (enojado, enojado) --- / código ---

--- /task ---

No dudes en utilizar las demás imágenes disponibles o crear las tuyas propias e incluirlas en el proyecto.

--- save ---
