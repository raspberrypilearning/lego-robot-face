## 添加眼睛

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">示例面中使用的 LED 矩阵连接到 Raspberry Pi <span style="color: #0faeb0">I2C</span>。 使用 I2C 的设备使用称为地址的特定编号进行连接。 当您使用两个矩阵时，每个矩阵都需要自己的地址。 </p>

--- task ---

在将它们连接起来之前，您需要遵循相关的 [组装说明](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){:target="_blank"}。 LED 阵列的组装需要进行一些焊接，因此在使用任何工具之前，请先获得成年人的许可。 您可以在此处按照我们的焊接指南进行操作。 <iframe width="560" height="315" src="https://www.youtube.com/embed/8Z-2wPWGnqE" title="YouTube 视频播放器" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe>

--- /task ---

这个项目中使用的矩阵都带有相同的地址，这意味着要让两个矩阵一起工作，其中一个需要一个新地址。 为此，需要更多的焊接。

--- task ---

使用焊接的试剂盒，所述接近 `A0` 的连接 **只有一个** 的矩阵。

![焊接和未焊接电路板的图像。](images/A0-soldering.jpg)

--- /task ---

--- task ---

将眼睛放在机器人脸上的方形眼窝中；使用松紧带固定它们并确保别针在顶部。

![图像显示安装在 LEGO® 表面的 8 x 8 阵列。](images/array_eyes.jpg)

--- /task ---

现在机器人面部的基本构建已经完成，您需要添加 Raspberry Pi 计算机并将您的组件连接到它。
