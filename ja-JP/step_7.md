## モーターで口を動かす

--- task ---

**Thonny** をプログラミングメニューから開き、新しいファイルを `robot_face.py` として保存して、 `classifier.py` 、 `labels.txt` 、8×8のドット画像と同じディレクトリに保存されていることを確認してください。

![robot_face.py を保存する場所のファイル構造を示す図。](images/file_structure.png)

--- /task ---

--- task ---

はじめに、 LEGO® Technic™ モーターを制御するためのインポート行を追加することから始めましょう。

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start:
line_highlights:
---

from buildhat import Motor

--- /code ---

--- /task ---

--- task ---

左右のモーター用に新しいオブジェクトを2つ作成しましょう。 この例では、右側のモーターはポートAに接続され、左側のモーターはポートBに接続されています。

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

mouth_r = Motor('A') 
mouth_l = Motor('B')
--- /code ---

--- /task ---

--- task ---

両方のモーターは、プログラムの起動時に `0` の位置で開始するようにします。

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 5
line_highlights:
---

mouth_r.run_to_position(0) 
mouth_l.run_to_position(0)
--- /code ---

--- /task ---

--- task ---

口のモーターを動かすための関数を作成しましょう。 これらは反対方向に回転する必要があるため、左側のモーターは負の値に回転し、右側のモーターは正の値に回転させます。 `blocking=False` を追加すると、両方のモーターが同時に回転できるようになります。

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 8
line_highlights:
---
def move_mouth (position, speed=100): 
    mouth_l.run_to_position(position * -1, speed, blocking=False) #負の位置に回転 
    mouth_r.run_to_position(position, speed, blocking=False) #正の位置に回転
--- /code ---

--- /task ---

--- task ---

コードを実行して、**シェル**の中で新しい関数をテストしましょう。

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
>>> move_mouth(45)
>>> move mouth(0)
--- /code ---

モーターが違う方向に動く場合は、ポートを切り替えてみてください。

--- /task ---

--- save ---
