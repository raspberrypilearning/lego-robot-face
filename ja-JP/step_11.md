## オブジェクトに対する感情的な反応

プロジェクトを終了するために、カメラが見ることができるものに応じて、ロボットの顔に異なる表情を表示させることができます。

![左側のコードは、カメラの前に保持されているさまざまな画像を示すカメラビューを示しています。 右側では、ロボットの顔が画像に反応します。](images/completed_project.gif)

--- task ---

インポートすることでスタート `分類子` と一緒に、あなたが以前に使用したファイルからクラスを `睡眠` 機能。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
from classifier import Classifier from time import sleep --- / code ---

--- /task ---

--- task ---

次に、分類子が認識できるオブジェクトのリストを作成します。 `しきい値` 調整して、分類器の認識を多かれ少なかれ正確にすることができます。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

saw_items = Classifier（label_file = "labels.txt"、model_file = "model.tflite"、threshold = 0.5） --- / code ---

--- /task ---

--- task ---

次に、オブジェクトをさまざまな感情にリンクする辞書を作成します。 あなたはあなたの周りにあるもの、またはあなたが印刷した画像に応じてあなた自身のオブジェクトと感情を選ぶことができます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

反応= {"ブロッコリー"： "ニュートラル"、 "ティーポット"： "ニュートラル"、 "ヘビ"： "怒り"、 "ホットドッグ"： "ハッピー"} --- / code ---

--- /task ---

--- task ---

`seen_items` リストにあるものをチェックするループを作成 `リアクション` ディクショナリに従って表情を表示できます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True： sleep（1） if saw_items.item！= saw_items.last_item： item = saw_items.item if item in set_face（faces [reactions[item]]） sleep（1） --- / code ---

--- /task ---

--- save ---
