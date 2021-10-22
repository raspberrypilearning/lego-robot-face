## 编程眉毛

第三个电机用于移动面部的眉毛。

--- task ---

为眉毛的马达设置一个对象。

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 3
line_highlights: 5
---
嘴巴_r = 马达('A') 嘴巴_l = 马达('B') 眉毛 = 马达('C')

--- /code ---

--- /task ---

--- task ---

确保您的大电机的位置使 **棒棒糖** 和 **圆** 对齐，并且您的脸的眉毛水平设置。 如果不是，您可能需要稍微调整您的构建。

![电机旋转，使棒棒糖和圆圈对齐。](images/motor_0.jpg)

![眉毛处于水平位置的机器人脸。](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

现在将电机设置为在程序启动时 `0`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights: 9
---
嘴巴_r.run_to_position(0) 嘴巴_l.run_to_position(0) 眉毛.run_to_position(0) --- /code ---

--- /task ---

此处将显示三个眉毛位置，但您可以创建更多位置。

- `0` 会使眉毛看起来水平
- `150` 将降低眉毛
- `-150` 会挑眉


--- task ---

添加获取当前眉毛位置的函数，如果它应该移动到的位置小于当前位置，则逆时针移动，否则顺时针移动。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---
def move_eyebrows (position): current_position = if position < current_position: rotation = '逆时针' else: rotation = '顺时针' 眉毛.run_to_position(position, direction = rotation)

--- /code ---

--- /task ---

--- task ---

运行您的代码并在 **Shell**测试您的新函数。

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights:
---
> > > move_eyebrows(-150) move_eyebrows(150) move_eyebrows(0) --- /code ---

--- /task ---

--- save ---
