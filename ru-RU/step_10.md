## Меняются лица

Теперь пришло время объединить все ваши функции, чтобы полностью изменить лицо.

--- task ---

Для начала вам нужно создать словарь для хранения различных выражений лица, которые вы хотите использовать. Это даст значения для двигателей рта, бровей и глаз.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

Faces = { "нейтральный": {"рот": 0, "right_eye": нейтральный, "left_eye": нейтральный, "брови": 0}, "счастливый": {"рот": 45, "right_eye": wide, "left_eye": wide, "брови": 150}, "angry": {"рот": - 20, "right_eye": сердитый, "left_eye": сердитый, "брови": - 150}, " sad ": {" рот ": - 45," right_eye ": look_down," left_eye ": look_down," брови ": - 40} } --- / code ---

--- /task ---

--- task ---

Теперь создайте функцию, которая установит рот, брови и глаза.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (лицо): change_eyes (лицо ["right_eye"], лицо ["left_eye"]) move_mouth (лицо ["рот"]) move_eyebrows (лицо ["брови"]) --- / code - -

--- /task ---

--- task ---

Запустите свой код, а затем используйте оболочку **** для проверки вашей новой функции.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face (faces ['angry']) set_face (faces ['happy']) set_face (faces ['нейтральные']) set_face (faces ['sad']) --- / code ---

--- /task ---

--- save ---
