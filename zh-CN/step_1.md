## 简介

[[[camera-bullseye]]]

在此项目中，您将使用乐高（ LEGO®）和一些电子元件组建一个机器的人脸。 您将使用现有的机器学习模型来帮助您的机器人脸识别不同的对象，并对其做出反应。

### 学习成果

--- no-print ---

您的机器人脸将能够识别一系列的物体并对其做出反应。 在这里您可以看到一个我们的机器人脸的范例。

![有关一个具有 LED 眼睛和持续变化表情的乐高  (LEGO®) 机器人脸的视频。](images/robot_face.gif)

您可以使用任何现有的乐高（ LEGO®） 组件和其他材料来制作您的机器人脸。 我们使用 [乐高LEGO® SPIKE™ Prime 套件](https://education.lego.com/en-gb/product/spike-prime)。

--- /no-print ---

--- print-only ---

![制作完成的图片：一个带有 LED 眼睛和微笑的表情的乐高 (LEGO®) 机器人脸。](images/robot_face.jpg)

--- /print-only ---

--- collapse ---
---
title: 您需要准备的材料
---
### 硬件

+ 一台树莓派电脑(Raspberry Pi)
+ 一个 Raspberry Pi Build HAT
+ 树莓派相机模块
+ 一根 30 厘米长的Raspberry Pi 相机模块带状电缆
+ 2 个小号乐高（LEGO®） Technic™ 马达
+ 1 个大号乐高（LEGO®）Technic™ 马达
+ 1块迷你面包板
+ 12支公对母跳线（20厘米长）
+ 2块[Adafruit 8×8 LED 矩阵](https://www.adafruit.com/product/1049) （或者类似的产品 — 组装和修改需要焊接）
+ 超长的堆叠排针
+ 各种乐高（LEGO®）组件（我们从 [LEGO® SPIKE™ Prime 套件](https://education.lego.com/en-gb/product/spike-prime)中选择了一些）
+ 20 毫米母对公接头扩展器。
+ 焊接套件

### 软件

打开一个终端并使用以下命令安装所需的库：

+ BuildHAT Python 库，用于控制 Build HAT

```
sudo pip3 install buildhat
```

+ TensorFlow 简库，示例模型和标签

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-tflite-runtime
```

+ Adafruit LED 矩阵库

```
pip3 install adafruit-circuitpython-ht16k33
```

### 下载

+ [图像分类测试文件](https://rpf.io/p/zh-CN/lego-robot-face-go){:target="_blank"}

--- /collapse ---

--- collapse ---
---
title: 您将学到什么
---

+ 使用乐高（LEGO®）构建更复杂的机制
+ 使用机器学习库来识别图像
+ 使用字典数据结构来控制面部表情

--- /collapse ---

--- collapse ---
---
title: 为教育者提供的额外信息
---

如果您需要打印此项目，请使用[适合打印的版本](https://projects.raspberrypi.org/zh-CN/projects/robot-face/print){:target="_blank"}.

[这里是本项目资源的链接](https://rpf.io/p/zh-CN/lego-robot-face-go){:target="_blank"}.

--- /collapse ---

在开始之前，您需要设置好您的 Raspberry Pi 并连接您的 Build HAT：

--- task ---

使用 M2 螺栓和螺母将您的 Raspberry Pi 安装到乐高（LEGO®）Maker Plate上，请确保 将Raspberry Pi 置于没有“边缘”的一侧：

 ![通过螺栓固定在洋红色乐高(LEGO®) Maker Plate上的Raspberry Pi。](images/build_11.jpg)

--- /task ---

以这种方式安装 Raspberry Pi 可以轻松访问（Raspberry Pi的）端口和 SD 卡插槽。 Maker Plate 可让您更轻松地将 Raspberry Pi 连接到仪表板的主要部件。

--- task ---

将 Build HAT 与 Raspberry Pi 对齐，请确保您可以看到 `This way up` 标签。 确保Build HAT准确滴覆盖了所有的 GPIO 引脚，然后用力按下。 （示例中使用了[堆叠头](https://www.adafruit.com/product/2223){:target="_blank"}，因此有更长的引脚。）

![显示GPIO 引脚穿过 Build HAT 的顶部的图片。](images/build_15.jpg) ![显示将 Buildhat 匹配到 Raspberry Pi的动画](images/haton.gif)

--- /task ---

现在利用 Build HAT 上的 7.5V 桶形插孔为您的 Raspberry Pi 供电，这也将用于驱动马达。

--- task ---

如果您尚未设置您的 Raspberry Pi，请按照以下步骤：

[设置你的Raspberry Pi](https://projects.raspberrypi.org/zh-CN/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Pi 启动后，单击 Raspberry 菜单按钮，然后选择“首选项”，然后选择“Raspberry Pi 配置”，打开 Raspberry Pi 配置工具。

单击“interfaces”选项卡并调整串口设置，如下所示：

![Raspberry Pi 操作系统的配置界面：启用串行端口，禁用串行控制台](images/configshot.jpg)

--- /task ---

--- task --- 您还需要按照以下说明安装 buildhat的 python 库：

--- collapse ---
---
title: 安装 buildhat Python 库
---

按下<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>，在 Raspberry Pi 上打开一个终端窗口。

在提示符后键入： `sudo pip3 install buildhat`

按 <kbd>回车</kbd> 并等待“installation completed”消息。

--- /collapse ---

--- /task ---
