## 目をプログラムする

LEDマトリックスは、ディスプレイに8×8ピクセルの画像を表示できます。 これらは、目のさまざまな動きを表示するために使用できます。

--- task ---

LEDディスプレイに画像を表示できるように、3つの新しいライブラリを追加します。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
buildhat輸入モーターから 輸入盤 adafruit_ht16k33.matrixインポートMatrix8x8から PILインポートイメージから

--- /code ---

--- /task ---

--- task ---

左目と右目を使用するようにオブジェクトを設定します。 `A0` パッドをはんだ付けしたものに応じて、異なるディスプレイで異なる画像を使用する場合は、後でコードを調整できます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C（） left_eye = Matrix8x8（i2c、address = 0x70） right_eye = Matrix8x8（i2c、address = 0x71） --- / code ---

--- /task ---

--- task ---

PILライブラリを使用すると、一部の画像を開いて保存できます。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

ニュートラル= Image.open（ "neutral.png"）。rotate（90） wide = Image.open（ "wide.png"）。rotate（90） angry = Image.open（ "angry.png"）。rotate （90） look_down = Image.open（ "look_down.png"）。rotate（90） --- / code ---

--- /task ---

--- task ---

LEDに表示される目を変更する新しい関数を記述します。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes（left、right）： left_eye.image（left） right_eye.image（right） --- / code ---

--- /task ---

--- task ---

あなたのコードを実行し、その後、使用 **シェル** 、あなたの新しい機能をテストします。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes（ニュートラル、ニュートラル） change_eyes（ワイド、ワイド） change_eyes（怒り、怒り） --- / code ---

--- /task ---

利用可能な他の画像を自由に使用するか、独自の画像を作成してプロジェクトに含めてください。

--- save ---
