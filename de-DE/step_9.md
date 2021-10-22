## Program the eyes

The LED matrices can show 8×8 pixel images on their displays. These can be used to display different motions of the eyes.

--- task ---

Add three new libraries to allow you to display images on the LED displays.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
from buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

Set up objects to use the left and right eye. For now, the images on each eye will be the same, but you can adjust your code later, if you want to use different images on the different displays, depending on which one you soldered the `A0` pads on.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() left_eye = Matrix8x8(i2c, address=0x70) right_eye = Matrix8x8(i2c, address=0x71) --- /code ---

--- /task ---

--- task ---

Using the PIL library, some of the images can be opened and stored.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

neutral = Image.open("neutral.png").rotate(90) wide = Image.open("wide.png").rotate(90) angry = Image.open("angry.png").rotate(90) look_down = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

Write a new function to change the eyes that are displayed on the LEDs.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes(left,right): left_eye.image(left) right_eye.image(right) --- /code ---

--- /task ---

--- task ---

Run your code and then use the **Shell** to test your new function.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes(neutral, neutral) change_eyes(wide, wide) change_eyes(angry, angry) --- /code ---

--- /task ---

Feel free to use the other images available, or to make your own and include them in the project.

--- save ---
