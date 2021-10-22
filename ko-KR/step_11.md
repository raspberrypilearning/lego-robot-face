## 사물에 대한 감정적 반응

프로젝트를 마무리하기 위해 카메라가 볼 수 있는 것에 따라 로봇 얼굴이 다른 표정을 표시하도록 할 수 있습니다.

![카메라 앞에 있는 다른 이미지를 보여주는 카메라 보기가 있는 왼쪽의 코드입니다. 오른쪽에서 로봇 얼굴이 이미지에 반응합니다.](images/completed_project.gif)

--- task ---

`sleep` 함수와 함께 이전에 사용한 파일에서 `Classifier` 클래스를 가져오는 것으로 시작합니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
from classifier import Classifier from time import sleep --- /code ---

--- /task ---

--- task ---

그런 다음 분류자가 인식할 수 있는 개체 목록을 만듭니다. `임계값` 조정하여 분류기가 인식에 어느 정도 정확하도록 할 수 있습니다.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

본_항목 = 분류자(label_file="labels.txt",model_file="model.tflite", 임계값=0.5) --- /코드 ---

--- /task ---

--- task ---

이제 사물을 다양한 감정에 연결하는 사전을 만드십시오. 주변에 있는 물건이나 출력한 이미지에 따라 자신만의 오브제와 감정을 선택할 수 있습니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

반응 = {"브로콜리":"중립","찻주전자":"중립","뱀":"화난","핫도그":"행복"} --- /코드 ---

--- /task ---

--- task ---

마지막으로 루프를 만들어 `see_items` `반응` 사전에 따라 표정을 표시할 수 있습니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep(1) if see_items.item != see_items.last_item: item = see_items.item if item in set_face(faces[reactions[item]]) sleep(1) --- /코드 ---

--- /task ---

--- save ---
