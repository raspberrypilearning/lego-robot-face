## Запрограммируйте глаза

Светодиодные матрицы могут отображать на своих дисплеях изображения размером 8 × 8 пикселей. Их можно использовать для отображения различных движений глаз.

--- task ---

Добавьте три новые библиотеки, позволяющие отображать изображения на светодиодных дисплеях.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
from buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

Настройте объекты, чтобы использовать левый и правый глаз. На данный момент изображения на каждом глазу будут одинаковыми, но вы можете изменить свой код позже, если вы хотите использовать разные изображения на разных дисплеях, в зависимости от того, к какому из них вы припаивали контактные площадки `A0`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C () left_eye = Matrix8x8 (i2c, address = 0x70) right_eye = Matrix8x8 (i2c, address = 0x71) --- / code ---

--- /task ---

--- task ---

Используя библиотеку PIL, можно открывать и сохранять некоторые изображения.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

нейтральный = Image.open ("нейтральный.png"). rotate (90) wide = Image.open ("wide.png"). rotate (90) angry = Image.open ("angry.png"). rotate (90) look_down = Image.open ("look_down.png"). Rotate (90) --- / code ---

--- /task ---

--- task ---

Напишите новую функцию для изменения глаз, отображаемых на светодиодах.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes (слева, справа): left_eye.image (слева) right_eye.image (справа) --- / code ---

--- /task ---

--- task ---

Запустите свой код, а затем используйте оболочку **** для проверки вашей новой функции.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes (нейтральный, нейтральный) change_eyes (широкий, широкий) change_eyes (сердитый, сердитый) --- / code ---

--- /task ---

Не стесняйтесь использовать другие доступные изображения или создавать свои собственные и включать их в проект.

--- save ---
