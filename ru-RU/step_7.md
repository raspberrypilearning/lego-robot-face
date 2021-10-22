## Моторизовать рот

--- task ---

Откройте **Thonny** из меню программирования и сохраните новый файл с именем `robot_face.py`и убедитесь, что сохранили его в том же каталоге, что и `classifier.py`, `labels.txt`и 8 × 8 пикселей. изображений.

![Файловая структура, показывающая, где должен храниться robot_face.py.](images/file_structure.png)

--- /task ---

--- task ---

Начните с добавления импорта, который вам понадобится для управления двигателями LEGO® Technic ™.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights:
---
from buildhat import Motor --- /code ---

--- /task ---

--- task ---

Создайте два новых объекта для левого и правого двигателей. В этом примере правый двигатель подключен к порту A, а левый - к порту B.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

outh_r = Мотор ('A') рот_l = Мотор ('B') --- / код ---

--- /task ---

--- task ---

Оба двигателя должны запускаться в положении `0` при запуске программы.

--- code ---
---
language: python filename: robot_face,py line_numbers: true line_number_start: 5
line_highlights:
---

mouth_r.run_to_position (0) mouth_l.run_to_position (0) --- / code ---

--- /task ---

--- task ---

Создайте функцию, которая будет двигать двигатели рта. Они должны вращаться в противоположных направлениях, поэтому левый двигатель будет вращаться на отрицательное значение, а правый - на положительное. Добавление `блокировки = False` заставит оба двигателя вращаться одновременно.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 8
line_highlights:
---
def move_mouth (position, speed = 100): mouth_l.run_to_position (position * -1, speed, blocking = False) # Перейти в отрицательное положение mouth_r.run_to_position (position, speed, blocking = False) # Перейти в положительное положение --- / код ---

--- /task ---

--- task ---

Запустите вашу программу, а затем проверьте новую функцию в оболочке ****.

--- code ---
---
язык: python имя_файла: номер_строки: ложь номер_строки_начало:
line_highlights:
---
> > > move_mouth (45) переместить рот (0) --- / code ---

Если ваши моторы движутся в неправильном направлении, попробуйте переключить их порты.

--- /task ---

--- save ---
