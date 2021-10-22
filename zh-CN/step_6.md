## 添加树莓派

对于这个项目，您最好使用 Build Plate 元素来安装 Raspberry Pi 和 Build HAT：

![显示洋红色 LEGO® 构建板的图像。](images/build_10.png)

--- task ---

使用 M2 螺栓和螺母将 Raspberry Pi 安装到构建板上，确保 Pi 位于平坦的一侧：

 ![Raspberry Pi 用螺栓固定在洋红色 LEGO® 构建板上。](images/build_11.jpg)

--- /task ---

以这种方式安装 Raspberry Pi 可以轻松访问端口和 SD 卡插槽。

### 安装相机并构建 HAT

在添加 Build HAT 之前，您首先需要将相机带状电缆连接到 Raspberry Pi 并将其穿过 Build HAT 中的孔。 如果您尚未将相机板连接到 Raspberry Pi，您可以按照以下说明进行连接： [相机模块](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)入门 {:target="_blank"}。

![显示 Raspberry Pi 摄像头模块连接到 Raspberry Pi 的动画。](images/connect-camera.gif)

--- task ---

将相机色带连接到 Raspberry Pi，但通过向上推黑色小夹子并将色带滑出，从色带松散端取下相机板：

![显示带有闭合夹子的摄像头板背面的图像。](images/build_12.jpg)

![图像显示了相机板的背面，打开的夹子和色带被移除。](images/build_13.jpg)

--- /task ---

--- task ---

将色带穿过 Build HAT 的底部并穿过顶部，确保色带没有扭曲： ![Picamera 丝带穿过 Build HAT 顶部的图像。](images/build_14.jpg)

--- /task ---

--- task ---

将 Build HAT 与 Raspberry Pi 对齐，确保您可以看到 `This way up` 标签。 确保所有 GPIO 引脚都被 HAT 覆盖，然后用力按下。 （该示例使用 [堆叠头](https://www.adafruit.com/product/2223){:target="_blank"}，这使得引脚更长。）

![GPIO 引脚穿过 Build HAT 顶部的图像。](images/build_15.jpg)

--- /task ---

--- 任务 --- 将相机重新连接到带状电缆的末端，确保它没有扭曲。

![连接到带状电缆的 Picamera 的图像。](images/build_16.jpg)

--- /task ---

--- 任务 --- 使用一些黑色螺栓将构建板连接到机器人面部的背面。 ![Maker Plate 和 Raspberry Pi 连接到机器人面部后部的图像。](images/build_17.jpg)

以这种方式安装 Raspberry Pi 可以最好地访问端口和引脚，这意味着您的桶形插孔可以轻松连接到为机器人面部供电。

--- /task ---

--- task ---

将您的小型 LEGO® Technic™ 电机连接到端口 A 和 B，准备控制嘴巴。

![两个小型 LEGO® Technic™ 电机连接到 Build HAT 上的端口 A 和 B 的图像。](images/build_18.jpg)

--- /task ---

--- task ---

将大型 LEGO® Technic™ 电机连接到端口 C，准备控制眉毛。

![显示连接到 Build HAT 端口 C 的大型 LEGO® Technic™ 电机的图像。](images/build_19.jpg)

--- /task ---

--- task ---

使用底部的粘合垫，将面包板粘在支撑大型 LEGO® 电机的框架顶部。

![显示粘在机器人面部机构顶部的面包板的图像。](images/build_20.jpg)

--- /task ---

--- task ---

通过将色带穿过支架下方并将摄像头楔入两侧的橡胶塞之间，将相机板安装在机器人面部顶部的支架中。

使用两侧的黑色凸耳用松紧带固定相机。

![图像显示了使用松紧带安装的前后摄像头板。](images/build_21.jpg)

--- /task ---

要将这对眼睛连接到 Raspberry Pi GPIO，首先需要使用面包板将它们连接在一起，然后从面包板连接到 GPIO 引脚。

--- task ---

使用八根公母跳线将面包板上每只眼睛的四个引脚连接在一起。 确保两个 VCC 引脚都在面包板的同一行中，两个 GND 引脚都在同一行中，依此类推。 然后连接到树莓派上的 3V3、GND、SDA 和 SCL 引脚，如下图所示。

![I2C 图。](images/eye_wiring.png)

--- /task ---

您的机器人面部现已构建、连接并准备好进行编程！





