## 添加眼睛

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">示例中使用的 连接到 Raspberry Pi <span style="color: #0faeb0">I2C</span>的LED 矩阵。 使用 I2C 的设备通过称为地址的特定编号进行连接。 当您使用两个矩阵时，每个矩阵都需要自己的地址。 </p>

--- task ---

在将它们连接起来之前，您需要遵循相关的 [组装说明](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){:target="_blank"}。 组装LED 阵列需要一些焊接工作。在使用任何工具之前，请先获得成年人的许可。 您可以按照我们此处的焊接指南进行操作。 <iframe width="560" height="315" src="https://www.youtube.com/embed/8Z-2wPWGnqE" title="YouTube 视频播放器" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe>

--- /task ---

本项目中使用的矩阵都有相同的默认地址，这意味着如果要让两个矩阵一起工作，其中一个矩阵将需要一个新地址。 因此，需要更多的焊接工作。

--- task ---

利用焊接套件，将其中一个矩阵的`A0` 焊上。

![已焊接和未焊接的电路板的图像。](images/A0-soldering.jpg)

--- /task ---

--- task ---

将眼睛放在机器人脸上的方形眼窝中；使用松紧带固定它们并确保管脚在顶部。

![安装了 8 x 8 阵列的乐高（LEGO®）人脸的图像。](images/array_eyes.jpg)

--- /task ---

现在机器人脸已经基本构建完成，您需要添加 Raspberry Pi 电脑并连接您的组件。
