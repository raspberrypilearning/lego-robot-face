## 对物体的情绪反应

为了完成项目，您可以根据相机可以看到的内容使机器人面部显示不同的表情。

![左侧的代码与相机视图显示不同的图像保持在相机前。 在右侧，机器人面部对图像做出反应。](images/completed_project.gif)

--- task ---

首先从您之前使用的文件中 `Classifier` `sleep` 函数。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
从分类器导入分类器 从时间导入睡眠 --- /code ---

--- /task ---

--- task ---

然后创建分类器可以识别的对象列表。 您可以 `阈值` 以使分类器或多或少地识别准确。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

see_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5) --- /code ---

--- /task ---

--- task ---

现在创建一个字典，将对象与不同的情绪联系起来。 您可以根据周围的物品或打印的图像选择自己的对象和情感。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

反应 = {“花椰菜”：“中性”，“茶壶”：“中性”，“蛇”：“愤怒”，“热狗”：“快乐”} --- /code ---

--- /task ---

--- task ---

最后，您可以创建一个循环， `seen_items` 列表中的内容，然后根据您的 `反应` 字典显示面部表情。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep(1) if seen_items.item != seen_items.last_item: item = seen_items.item if item in set_face(faces[reactions[item]]) sleep(1) - - /代码  - -

--- /task ---

--- save ---
