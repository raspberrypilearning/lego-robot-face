## 사물에 대한 감정적 반응

프로젝트를 마무리하기 위해 카메라가 볼 수 있는 것에 따라 로봇 얼굴이 다른 표정을 표시하도록 할 수 있습니다.

![좌측의 코드: 카메라의 앞에 보관 유지되고 있는 다양한 화상을 나타내는 카메라 뷰를 나타내고 있는 이미지 오른쪽에서 로봇 얼굴이 이미지에 반응하는 이미지](images/completed_project.gif)

--- task ---

`sleep` 함수와 함께 이전에 사용한 파일에서 `Classifier` 클래스를 가져오는 것으로 시작합니다.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 7
line_highlights:
---
from classifier import Classifier 
from time import sleep
--- /code ---

--- /task ---

--- task ---

그런 다음 classifier (분류기) 가 인식할 수 있는 개체 목록을 만듭니다. `threshold`라는 임계값을 조정하여 Classifier가 더 정확하게 인식하도록 할 수 있습니다.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 31
line_highlights:
---

seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)
--- /code ---

--- /task ---

--- task ---

이제 사물을 다양한 감정에 연결하는 딕셔너리를 만드십시오. 주변에 있는 물건이나 출력한 이미지에 따라 자신만의 오브제와 감정을 선택할 수 있습니다.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 33
line_highlights:
---

reactions = {"broccoli":"neutral","teapot":"neutral","snake":"angry","hotdog":"happy"}
--- /code ---

--- /task ---

--- task ---

`seen_items` 리스트에 무엇이 있는지 2초에 한번씩 체크하는 루프를 작성하여, `reaction` 딕셔너리에서 표정을 표시할 수 있습니다.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 61
line_highlights:
---
while True: 
    sleep(1) 
    if seen_items.item != seen_items.last_item: 
        item = seen_items.item 
        if item in reactions.keys(): 
            set_face(faces[reactions[item]]) 
    sleep(1)
--- /code ---

--- /task ---

--- save ---
