## 입 움직이기

--- task ---

**Thonny**프로그래밍 메뉴를 열어, `robot_face.py` 라는 새로운 파일을 만들고 저장하고, `classifier.py`, `labels.txt`, 그리고 8×8 픽셀 아트 이미지를 같은 디렉토리에 추가합니다.

![robots_face.py가 저장되어야 하는 위치를 보여주는 파일 구조](images/file_structure.png)

--- /task ---

--- task ---

먼저 LEGO® Technic™ 모터를 제어하는 데 필요한 라이브러리를 추가하세요.

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

왼쪽 및 오른쪽 모터에 대해 두 개의 새 객체를 만듭니다. 이 예에서 오른쪽 모터는 포트 A에 연결되고 왼쪽 모터는 포트 B에 연결됩니다.

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

두 모터는 프로그램이 시작될 때 `0` 포지션에서 시작되어야 합니다.

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

마우스 모터를 움직일 함수를 만듭니다. 반대 방향으로 회전해야 하므로 왼쪽 모터는 음수 값으로 오른쪽 모터는 양수 값으로 회전하도록 해야 합니다. `blocking=False` 를 추가하면 두 모터가 동시에 회전합니다.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 8
line_highlights:
---
def move_mouth (position, speed=100): 
    mouth_l.run_to_position(position * -1, speed, blocking=False) #반대 방향으로(역방향) 회전 
    mouth_r.run_to_position(position, speed, blocking=False) #진행 방향으로(순방향) 회전
--- /code ---

--- /task ---

--- task ---

**Shell**에서 새 기능을 테스트하세요.

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

모터가 잘못된 방향으로 움직이면 포트를 전환해 보세요.

--- /task ---

--- save ---
