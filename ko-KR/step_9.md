## 눈을 프로그래밍

LED 매트릭스는 디스플레이에 8×8 픽셀 이미지를 표시할 수 있습니다. 이들은 눈의 다양한 움직임을 표시하는 데 사용할 수 있습니다.

--- task ---

LED 디스플레이에 이미지를 표시할 수 있도록 3개의 새 라이브러리를 추가합니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 2-4
---
buildhat에서 가져오기 모터 가져오기 보드 에서 adafruit_ht16k33.matrix 가져오기 Matrix8x8 에서 PIL 가져오기 이미지

--- /code ---

--- /task ---

--- task ---

왼쪽 눈과 오른쪽 눈을 사용하도록 개체를 설정합니다. `A0` 패드를 납땜한 디스플레이에 따라 다른 디스플레이에서 다른 이미지를 사용하려는 경우 나중에 코드를 조정할 수 있습니다.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 13
line_highlights:
---

i2c = board.I2C() left_eye = Matrix8x8(i2c, 주소=0x70) right_eye = Matrix8x8(i2c, 주소=0x71) --- /code ---

--- /task ---

--- task ---

PIL 라이브러리를 사용하여 일부 이미지를 열고 저장할 수 있습니다.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---

중립 = Image.open("neutral.png").rotate(90) 와이드 = Image.open("wide.png").rotate(90) 화가 = Image.open("angry.png").rotate (90) look_down = Image.open("look_down.png").rotate(90) --- /code ---

--- /task ---

--- task ---

LED에 표시되는 눈을 변경하는 새 함수를 작성하십시오.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 38
line_highlights:
---
def change_eyes(left, right): left_eye.image(left) right_eye.image(right) --- /code ---

--- /task ---

--- task ---

코드를 실행한 다음 **Shell** 을 사용하여 새 기능을 테스트합니다.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > change_eyes(중립, 중립) change_eyes(와이드, 와이드) change_eyes(앵그리, 화난) --- /code ---

--- /task ---

사용 가능한 다른 이미지를 자유롭게 사용하거나 직접 만들어 프로젝트에 포함할 수 있습니다.

--- save ---
