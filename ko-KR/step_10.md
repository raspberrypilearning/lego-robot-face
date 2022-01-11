## 얼굴 바꾸기

이제 얼굴 전체를 변경하기 위해 다양한 기능을 모두 사용할 때입니다.

--- task ---

먼저 사용하려는 다양한 표정을 저장할 딕셔너리를 만들어야 합니다. 이것은 입 모터, 눈썹 모터 및 눈에 대한 값을 제공합니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

faces = { "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0}, "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":150}, "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":-150}, "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

이제 입, 눈썹, 눈을 설정할 함수를 만듭니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (face): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code ---

--- /task ---

--- task ---

코드를 실행한 다음 **Shell** 을 사용하여 새 기능을 테스트합니다.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['angry']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
