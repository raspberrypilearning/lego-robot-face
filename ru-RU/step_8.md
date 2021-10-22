## Запрограммируйте брови

Третий мотор используется для перемещения бровей лица.

--- task ---

Установите объект для мотора бровей.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 3
line_highlights: 5
---
mouth_r = Мотор ('A') рот_l = Мотор ('B') брови = Мотор ('C')

--- /code ---

--- /task ---

--- task ---

Убедитесь, что ваш большой мотор расположен так, что леденец **** и круг **** выровнены, а брови вашего лица расположены горизонтально. Если это не так, возможно, вам придется немного скорректировать вашу сборку.

![Мотор повернулся так, что леденец и круг выровнялись.](images/motor_0.jpg)

![Лицо робота с бровями в горизонтальном положении.](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

Теперь установите двигатель в положение `0` при запуске программы.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights: 9
---
mouth_r.run_to_position (0) mouth_l.run_to_position (0) eyebrows.run_to_position (0) --- / code ---

--- /task ---

Здесь будут показаны три положения бровей, но вы можете создать и другие.

- `0` сделает брови горизонтальными
- `150` понизит брови
- `-150` поднимет брови


--- task ---

Добавьте функцию, которая получает текущее положение брови, и если положение, в которое она должна переместиться, меньше текущей, она будет двигаться против часовой стрелки, в противном случае она будет двигаться по часовой стрелке.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---
def move_eyebrows (position): current_position = eyebrows.get_aposition () если позиция < current_position: Rotation = 'против часовой стрелки' else: Rotation = 'clockwise' eyebrows.run_to_position (position, direction = вращение)

--- /code ---

--- /task ---

--- task ---

Запустите свой код и протестируйте новую функцию в оболочке ****.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights:
---
> > > move_eyebrows (-150) move_eyebrows (150) move_eyebrows (0) --- / code ---

--- /task ---

--- save ---
