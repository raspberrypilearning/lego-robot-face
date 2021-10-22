## 顔を変える

今度は、さまざまな機能をすべてまとめて、顔全体を変えましょう。

--- task ---

まず、使用したいさまざまな表情を保存するための辞書を作成する必要があります。 これにより、口のモーター、眉のモーター、および目の値が得られます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

顔= { "neutral"：{"mouth"：0、 "right_eye"：neutral、 "left_eye"：neutral、 "eyebrows"：0}、 "happy"：{"mouth"：45、 "right_eye"： wide、 "left_eye"：wide、 "eyebrows"：150}、 "angry"：{"mouth"：-20、 "right_eye"：angry、 "left_eye"：angry、 "eyebrows"：-150}、 "悲しい "：{"口 "：-45、" right_eye "：look_down、" left_eye "：look_down、"眉毛 "：-40} } --- / code ---

--- /task ---

--- task ---

次に、口、眉、目を設定する関数を作成します。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face（face）： change_eyes（face ["right_eye"]、face ["left_eye"]） move_mouth（face ["mouth"]） move_eyebrows（face ["eyebrows"]） --- / code- -

--- /task ---

--- task ---

あなたのコードを実行し、その後、使用 **シェル** 、あなたの新しい機能をテストします。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face（faces ['angry']） set_face（faces ['happy']） set_face（faces ['neutral']） set_face（faces ['sad']） --- / code ---

--- /task ---

--- save ---
