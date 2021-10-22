## 얼굴 바꾸기

이제 얼굴 전체를 변경하기 위해 다양한 기능을 모두 사용할 때입니다.

--- task ---

먼저 사용하려는 다양한 표정을 저장할 사전을 만들어야 합니다. 이것은 입 모터, 눈썹 모터 및 눈에 대한 값을 제공합니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

얼굴 = { "중립":{"입":0, "오른쪽 눈":중립, "왼쪽 눈":중립, "눈썹":0}, "행복":{"입":45, "오른쪽 눈": 와이드, "left_eye":와이드, "눈썹":150}, "화난":{"입":-20, "right_eye":화가, "left_eye":화가, "눈썹":-150}, " 슬픈":{"입":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

이제 입, 눈썹, 눈을 설정할 함수를 만듭니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face(얼굴): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code - --

--- /task ---

--- task ---

코드를 실행한 다음 **Shell** 을 사용하여 새 기능을 테스트합니다.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['화난']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
