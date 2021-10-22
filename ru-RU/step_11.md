## Эмоциональные реакции на предметы

Чтобы завершить проект, вы можете заставить лицо робота отображать разные выражения в зависимости от того, что видит камера.

![Код слева с изображением камеры, показывающим различные изображения, находящиеся перед камерой. Справа лицо робота реагирует на изображения.](images/completed_project.gif)

--- task ---

Начните с импорта `Classifier` из файла, который вы использовали ранее, вместе с функцией `sleep`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
из классификатора импорт классификатора из времени импорт сна --- / код ---

--- /task ---

--- task ---

Затем создайте список объектов, которые может распознать классификатор. Вы можете настроить порог `` позже, чтобы классификатор был более или менее точен при его распознавании.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

visible_items = Классификатор (label_file = "labels.txt", model_file = "model.tflite", threshold = 0.5) --- / code ---

--- /task ---

--- task ---

Теперь создайте словарь, который связывает объекты с разными эмоциями. Вы можете выбирать свои собственные объекты и эмоции в зависимости от того, что вас окружает, или изображений, которые вы распечатали.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

реакции = {"брокколи": "нейтральный", "чайник": "нейтральный", "змея": "сердитый", "хот-дог": "счастливый"} --- / code ---

--- /task ---

--- task ---

Наконец, вы можете создать цикл для проверки того, что находится в `visible_items` каждые две секунды, а затем отображать выражение лица в соответствии со своим словарем `реакций`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep (1) if visible_items.item! = visible_items.last_item: item = visible_items.item если элемент в set_face (faces [Reaction[item]]) sleep (1) --- / код ---

--- /task ---

--- save ---
