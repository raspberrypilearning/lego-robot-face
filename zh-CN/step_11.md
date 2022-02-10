## 对物体的情绪反应

为了完善本项目，您可以让机器人脸依据相机看到的内容而显示不同的表情。

![左侧是代码与相机视图，显示了在相机镜头前的不同图像。 右侧是机器人脸对该图像做出反应。](images/completed_project.gif)

--- task ---

首先从您之前使用的文件中导入 `Classifier` 和`sleep` 函数。

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

然后创建一个宝行分类器可以识别的对象的列表。 您可以通过分类器的 `阈值` 来调节它的识别准确度。

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 31
line_highlights:
---

see_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5) 
--- /code ---

--- /task ---

--- task ---

现在创建一个字典，将对象与不同的情绪联系起来。 您可以依据自身周围的物品或打印的图片来选择对象和情感。

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

最后，您可以创建一个循环，每隔两秒，依据 `seen_items` 列表中的内容，显示`reactions` 中相应的面部表情。

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
