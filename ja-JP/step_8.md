## 眉毛のプログラムを作る

3つ目のモーターは、顔の眉毛を動かすために使います。

--- task ---

眉毛のモーターのオブジェクトを設定します。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 3
line_highlights: 5
---
mouth_r = Motor('A') mouth_l = Motor('B') eyebrows = Motor('C')

--- /code ---

--- /task ---

--- task ---

大きなモーターの**ロリポップ**と**サークル**が揃うように配置されていることと、顔の眉毛が水平に設定されていることを確認しましょう。 そうなっていない場合は調整しましょう。

![ロリポップと円が揃うようにモーターを回転させた図。](images/motor_0.jpg)

![眉を水平にしたロボットの顔の図。](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

続けて、プログラムの開始時に、モーターを `0` の位置に回転するようにセットします。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights: 9
---
mouth_r.run_to_position(0) mouth_l.run_to_position(0) eyebrows.run_to_position(0) --- /code ---

--- /task ---

ここでは眉のための位置を3つ用意しますが、さらに作ることもできます。

- `0` は、眉を水平にします
- `150` 眉を下げます
- `-150` 眉を上げます


--- task ---

現在の眉の位置を取得する関数を追加しましょう。移動先の位置が現在の位置よりも小さい場合は反時計回りに移動し、そうでない場合は時計回りに移動します。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---
def move_eyebrows (position): current_position = eyebrows.get_aposition() if position < current_position: rotation = 'anticlockwise' else: rotation = 'clockwise' eyebrows.run_to_position(position, direction = rotation)

--- /code ---

--- /task ---

--- task ---

コードを実行して、**シェル**の中で新しい関数をテストしましょう。

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights:
---
> > > move_eyebrows(-150) move_eyebrows(150) move_eyebrows(0) --- /code ---

--- /task ---

--- save ---
