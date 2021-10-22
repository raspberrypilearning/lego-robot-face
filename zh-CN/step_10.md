## 变脸

现在是时候将所有不同的功能结合在一起来改变整张脸了。

--- task ---

首先，您需要创建一个字典来存储您要使用的不同面部表情。 这将给出嘴部马达、眉毛马达和眼睛的值。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

面孔 = { “中性”：{“嘴”：0，“右眼”：中性，“左眼”：中性，“眉毛”：0}， “快乐”：{“嘴”：45，“右眼”：宽, "left_eye":wide, "eyebrows":150}, "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":-150}, "悲伤":{"嘴":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

现在创建一个函数来设置嘴巴、眉毛和眼睛。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (face): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code - ——

--- /task ---

--- task ---

运行您的代码，然后使用 **Shell** 来测试您的新函数。

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['angry']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
