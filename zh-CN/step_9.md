## 给眼睛编程

LED 矩阵可以在其显示器上显示 8×8 像素的图像。 这些可用于显示眼睛的不同运动。

--- task ---

添加三个新库以允许您在 LED 显示屏上显示图像。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
from buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

设置对象以使用左眼和右眼。 目前，每只眼睛上的图像都是相同的，但如果您想在不同的显示器上使用不同的图像，您可以稍后调整代码，具体取决于您将 `A0` 焊盘焊接在哪个显示器上。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() left_eye = Matrix8x8(i2c, address=0x70) right_eye = Matrix8x8(i2c, address=0x71) --- /code ---

--- /task ---

--- task ---

使用 PIL 库，可以打开和存储一些图像。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

中性 = Image.open("neutral.png").rotate(90) 宽 = Image.open("wide.png").rotate(90) 生气 = Image.open("angry.png").rotate (90) look_down = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

编写一个新函数来改变 LED 上显示的眼睛。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes(left,right): left_eye.image(left) right_eye.image(right) --- /code ---

--- /task ---

--- task ---

运行您的代码，然后使用 **Shell** 来测试您的新函数。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes（中性，中性） change_eyes（宽，宽） change_eyes（愤怒，愤怒） --- /code ---

--- /task ---

随意使用其他可用的图像，或者制作自己的图像并将它们包含在项目中。

--- save ---
