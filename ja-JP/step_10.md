## 顔を変える

今度は、さまざまな機能をすべてまとめて、顔全体を変えましょう。

--- task ---

まず、使用したいさまざまな表情を保存するための辞書を作成する必要があります。 これによって、口のモーター、眉のモーター、目のための値を得ることができます。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

faces = { "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0}, "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":150}, "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":-150}, "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

口、眉、目を設定する関数を作成しましょう。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (face): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code ---

--- /task ---

--- task ---

コードを実行し、**シェル**を使って新しい関数をテストしましょう。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['angry']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
