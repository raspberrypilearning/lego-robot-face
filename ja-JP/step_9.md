## 目のプログラムを作る

LEDマトリックスは、ディスプレイ上に8×8ピクセルの画像を表示できます。 これらは、さまざまな目の動きを表示するために使用できます。

--- task ---

LEDディスプレイに画像を表示できるように、新しいライブラリを3つ追加します。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
from buildhat import Motor import board from adafruit_ht16k33.matrix import Matrix8x8 from PIL import Image

--- /code ---

--- /task ---

--- task ---

左目と右目を使用するようにオブジェクトを設定します。 今のところ、それぞれの目の画像は同じですが、 異なるディスプレイに異なる画像を使いたい場合は、`A0` パッドをはんだ付けしたほうに応じて、後でコードを調整できます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() left_eye = Matrix8x8(i2c, address=0x70) right_eye = Matrix8x8(i2c, address=0x71) --- /code ---

--- /task ---

--- task ---

PIL ライブラリを使用して、いくつかの画像を開いて格納します。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

neutral = Image.open("neutral.png").rotate(90) wide = Image.open("wide.png").rotate(90) angry = Image.open("angry.png").rotate(90) look_down = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

LEDに表示される目を変更するために、新しい関数を記述しましょう。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes(left,right): left_eye.image(left) right_eye.image(right) --- /code ---

--- /task ---

--- task ---

コードを実行し、**シェル**を使って新しい関数をテストしましょう。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes(neutral, neutral) change_eyes(wide, wide) change_eyes(angry, angry) --- /code ---

--- /task ---

利用可能な他の画像を自由に使用するか、独自の画像を作成してプロジェクトに含めてください。

--- save ---
