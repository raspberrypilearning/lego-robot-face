## 物に表情で反応させる

カメラが見たものに応じて、ロボットの顔にいろいろな表情をさせて、プロジェクトを完成させましょう。

![左側のコードは、カメラの前に保持されているさまざまな画像を示すカメラビューを示しています。 右側では、ロボットの顔が画像に反応します。](images/completed_project.gif)

--- task ---

まずは、 `Classifier` クラスと、`sleep` 関数を、前から使用しているファイルにインポートしましょう。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
from classifier import Classifier from time import sleep --- /code ---

--- /task ---

--- task ---

次に、認識できる分類のオブジェクトのリストを作成します。 分類器の認識を多少正確にするために、後で`しきい値`を調整できます。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5) --- /code ---

--- /task ---

--- task ---

次に、オブジェクトをさまざまな表情にリンクする辞書を作成します。 身の回りにあるものや印刷した画像に応じて、その選んだ物と感情を決めることができます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

reactions = {"broccoli":"neutral","teapot":"neutral","snake":"angry","hotdog":"happy"} --- /code ---

--- /task ---

--- task ---

最後に、 `seen_items` リストにあるものを 2 秒ごとにチェックするループを作成して、 `reactions` の辞書に従って表情を表示させます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep(1) if seen_items.item != seen_items.last_item: item = seen_items.item if item in reactions.keys(): set_face(faces[reactions[item]]) sleep(1) --- /code ---

--- /task ---

--- save ---
