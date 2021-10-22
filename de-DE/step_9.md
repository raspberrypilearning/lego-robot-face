## Programmieren Sie die Augen

Die LED-Matrizen können auf ihren Displays 8×8-Pixel-Bilder anzeigen. Diese können verwendet werden, um verschiedene Augenbewegungen darzustellen.

--- task ---

Fügen Sie drei neue Bibliotheken hinzu, damit Sie Bilder auf den LED-Displays anzeigen können.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
aus buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

Richten Sie Objekte ein, um das linke und rechte Auge zu verwenden. Vorerst sind die Bilder auf jedem Auge gleich, aber Sie können Ihren Code später anpassen, wenn Sie unterschiedliche Bilder auf den verschiedenen Displays verwenden möchten, je nachdem, auf welchem Sie die `A0` Pads gelötet haben.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() linkes_auge = Matrix8x8(i2c, Adresse=0x70) rechtes_auge = Matrix8x8(i2c, Adresse=0x71) --- /code ---

--- /task ---

--- task ---

Mithilfe der PIL-Bibliothek können einige der Bilder geöffnet und gespeichert werden.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

neutral = Image.open("neutral.png").rotate(90) wide = Image.open("wide.png").rotate(90) wütend = Image.open("angry.png").rotate (90) look_down = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

Schreiben Sie eine neue Funktion, um die auf den LEDs angezeigten Augen zu ändern.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes(left,right): left_eye.image(left) right_eye.image(right) --- /code ---

--- /task ---

--- task ---

Führen Sie Ihren Code aus und verwenden Sie dann die **Shell** , um Ihre neue Funktion zu testen.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes(neutral, neutral) change_eyes(wide, wide) change_eyes(wütend, wütend) --- /code ---

--- /task ---

Fühlen Sie sich frei, die anderen verfügbaren Bilder zu verwenden oder Ihre eigenen zu erstellen und in das Projekt aufzunehmen.

--- save ---
