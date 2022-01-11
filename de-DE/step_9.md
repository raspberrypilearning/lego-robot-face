## Programmierung der Augen

Die LED-Matrizen können auf ihren Displays 8×8-Pixel-Bilder anzeigen. Diese können verwendet werden, um verschiedene Augenbewegungen darzustellen.

--- task ---

Füge drei neue Bibliotheken hinzu, damit du Bilder auf den LED-Displays anzeigen kannst.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
from buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

Richte Objekte ein, um das linke und rechte Auge zu verwenden. Vorerst sind die Bilder auf jedem Auge gleich, aber du kannst deinen Code später anpassen, wenn du unterschiedliche Bilder auf den verschiedenen Displays verwenden möchtest. Das ist durch unterschiedliche Adressen möglich, die du durch das verlöten der `A0` Pads festgelegt hast.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() auge_links = Matrix8x8(i2c, address=0x70) auge_rechts = Matrix8x8(i2c, address=0x71) --- /code ---

--- /task ---

--- task ---

Mithilfe der PIL-Bibliothek können Bilder geöffnet und gespeichert werden.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

neutral = Image.open("neutral.png").rotate(90) grosz = Image.open("wide.png").rotate(90) veraergert = Image.open("angry.png").rotate(90) hinunterschauen = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

Schreibe eine neue Funktion, um die auf den LEDs angezeigten Augen zu ändern.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def wechsle_augen(links,rechts): auge_links.image(links) auge_rechts.image(rechts) --- /code ---

--- /task ---

--- task ---

Führe deinen Code aus und verwende dann die **Shell**, um deine neue Funktion zu testen.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > wechsle_augen(neutral, neutral) wechsle_augen(grosz, grosz) wechsle_augen(veraergert, veraergert) --- /code ---

--- /task ---

Wenn du magst kannst du die anderen verfügbaren Bilder verwenden oder deine eigenen erstellen und in das Projekt aufnehmen.

--- save ---
