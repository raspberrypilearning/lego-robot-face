## 입을 움직이다

--- task ---

프로그래밍 메뉴에서 **Thonny** 을 열고 `robot_face.py` `classifier.py`, `labels.txt`및 8×8 픽셀 아트와 동일한 디렉토리에 저장해야 합니다. 이미지.

![robots_face.py가 저장되어야 하는 위치를 보여주는 파일 구조.](images/file_structure.png)

--- /task ---

--- task ---

먼저 LEGO® Technic™ 모터를 제어하는 데 필요한 가져오기를 추가하세요.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights:
---
from buildhat import Motor --- /code ---

--- /task ---

--- task ---

왼쪽 및 오른쪽 모터에 대해 두 개의 새 개체를 만듭니다. 이 예에서 오른쪽 모터는 포트 A에 연결되고 왼쪽 모터는 포트 B에 연결됩니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

mouth_r = 모터('A') mouth_l = 모터('B') --- /코드 ---

--- /task ---

--- task ---

두 모터는 프로그램이 시작될 때 `0`

--- code ---
---
language: python filename: robot_face,py line_numbers: true line_number_start: 5
line_highlights:
---

mouth_r.run_to_position(0) mouth_l.run_to_position(0) --- /코드 ---

--- /task ---

--- task ---

마우스 모터를 움직일 함수를 만듭니다. 반대 방향으로 회전해야 하므로 왼쪽 모터는 음수 값으로 오른쪽 모터는 양수 값으로 회전합니다. `blocking=False` 추가하면 두 모터가 동시에 회전합니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 8
line_highlights:
---
def move_mouth (position, speed=100): mouth_l.run_to_position(position * -1, speed, blocking=False) #음수 위치 전환 mouth_r.run_to_position(position, speed, blocking=False) #양수 위치 --- /코드 ---

--- /task ---

--- task ---

**Shell**에서 새 기능을 테스트하십시오.

--- code ---
---
언어: 파이썬 파일 이름: line_numbers: false line_number_start:
line_highlights:
---
> > > move_mouth(45) 입 이동(0) --- /code ---

모터가 잘못된 방향으로 움직이면 포트를 전환해 보십시오.

--- /task ---

--- save ---
