## 机动嘴巴

--- task ---

从编程菜单中打开 **Thonny** `robots_face.py`的新文件，并确保将其保存在与 `classifier.py`、 `labels.txt`和 8×8 像素艺术相同的目录中图片。

![显示 robots_face.py 应存储位置的文件结构。](images/file_structure.png)

--- /task ---

--- task ---

首先添加控制 LEGO® Technic™ 电机所需的导入。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights:
---
from buildhat import Motor --- /code ---

--- /task ---

--- task ---

为左右电机创建两个新对象。 在此示例中，右侧电机连接到端口 A，左侧电机连接到端口 B。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start:
line_highlights: 3,4
---
from buildhat import Motor

口_r =电机（'A'） _l =电机（'B'） ---/代码---

--- /task ---

--- task ---

程序启动时，两个电机都应在 `0`

--- code ---
---
language: python filename: robot_face,py line_numbers: true line_number_start: 5
line_highlights:
---

嘴巴_r.run_to_position(0) 嘴巴_l.run_to_position(0) --- /code ---

--- /task ---

--- task ---

创建一个可以移动嘴部电机的函数。 它们需要以相反的方向转动，因此左侧电机将转为负值，而右侧电机将转为正值。 添加 `blocks=False` 将使两个电机同时转动。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 8
line_highlights:
---
DEF move_mouth（位置，速度= 100）： mouth_l.run_to_position（位置* -1，速度，阻断=假）#Turn到负位置 mouth_r.run_to_position（位置，速度，阻断=假）#Turn到正向位置 - - /代码  - -

--- /task ---

--- task ---

运行您的程序，然后在 **Shell**测试您的新函数。

--- code ---
---
语言：python 文件名： line_numbers：false line_number_start：
line_highlights:
---
> > > move_mouth(45) 移动嘴(0) --- /code ---

如果您的电机朝错误的方向移动，请尝试切换它们的端口。

--- /task ---

--- save ---
