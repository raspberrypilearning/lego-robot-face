## 简介

在这个项目的过程中，您将使用 LEGO® 和电子元件的组合构建一个机器人脸。 然后，您将使用现有的机器学习模型来帮助您的面部识别不同的对象并对其做出反应。

### 学习成果

--- no-print ---

您的机器人面部将能够识别一系列物体并做出反应。 在这里您可以看到我们的机器人面孔示例。

![由 LEGO® 制成的机器人脸的视频，带有 LED 眼睛和不断变化的表情。](images/robot_face.gif)

您应该使用任何可用的 LEGO® 和其他材料构建您的机器人脸。 我们使用了 [LEGO® SPIKE™ Prime 套件](https://education.lego.com/en-gb/product/spike-prime)。

--- /no-print ---

--- print-only ---

![已完成项目的图片：由 LEGO® 制成的机器人脸，带有 LED 眼睛和微笑的表情。](images/robot_face.jpg)

--- /print-only ---

--- collapse ---
---
title: 你需要准备什么
---
### 硬件

+ 一台树莓派电脑
+ 树莓派构建 HAT
+ 树莓派相机模块
+ 一根 30 厘米的树莓派相机带状电缆
+ 2 个小型 LEGO® Technic™ 电机
+ 1 个大型 LEGO® Technic™ 马达
+ 1× 迷你面包板
+ 12×公对母跳线（20cm）
+ 2× [Adafruit 8×8 LED 矩阵](https://www.adafruit.com/product/1049) （或类似的——需要一些焊接来组装和修改）
+ 超长堆叠排针
+ 各种各样的 LEGO®（我们使用了 [LEGO® SPIKE™ Prime 套件](https://education.lego.com/en-gb/product/spike-prime)一个选择）
+ 20 毫米 FM 接头扩展器。
+ 焊接套件

### 软件

打开终端并使用以下命令安装所需的库：

+ BuildHAT Python 库，用于控制 Build HAT

```
须藤 pip3 安装 buildhat
```

+ TensorFlow Lite 库和示例模型和标签

```
echo "deb https://packages.cloud.google.com/aptcoral-edgetpu-stable main" |须藤三通/etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-tflite-runtime
```

+ Adafruit LED 矩阵库

```
pip3 install adafruit-circuitpython-ht16k33
```

### 下载

+ [图像分类器测试文件](http://rpf.io/p/en/lego-robot-face-go){:target="_blank"}

--- /collapse ---

--- collapse ---
---
title: 你将学到什么
---

+ 使用 LEGO® 构建更复杂的机制
+ 使用机器学习库识别图像
+ 使用字典数据结构来控制面部表情

--- /collapse ---

--- collapse ---
---
给教师的其他信息
---

如果您需要打印此项目，请使用[打印友好版本 printer-friendly version ](https://projects.raspberrypi.org/en/projects/robot-face/print){:target="_blank"}.

[这是该项目](http://rpf.io/p/en/robot-face-go){:target="_blank"} 资源的链接。

--- /collapse ---

在开始之前，您需要设置您的 Raspberry Pi 计算机并连接您的 Build HAT：

--- task ---

使用 M2 螺栓和螺母将您的 Raspberry Pi 安装到乐高积木板上，确保 Raspberry Pi 位于没有“边缘”的一侧：

 ![树莓派用螺栓固定在洋红色乐高积木板上。](images/build_11.jpg)

--- /task ---

以这种方式安装 Raspberry Pi 可以轻松访问端口和 SD 卡插槽。 Build Plate 可让您更轻松地将 Raspberry Pi 连接到仪表板的主要结构。

--- task ---

将 Build HAT 与 Raspberry Pi 对齐，确保您可以看到 `This way up` 标签。 确保所有 GPIO 引脚都被 HAT 覆盖，然后用力按下。 （该示例使用 [堆叠头](https://www.adafruit.com/product/2223){:target="_blank"}，这使得引脚更长。）

![GPIO 引脚穿过 Build HAT 顶部的图像。](images/build_15.jpg) ![动画显示 Buildhat 适合 Raspberry Pi](images/haton.gif)

--- /task ---

您现在应该使用 Build HAT 上的 7.5V 桶形插孔为您的 Raspberry Pi 供电，这将允许您使用电机。

--- task ---

如果您还没有这样做，请按照以下说明设置您的 Raspberry Pi：

[设置你的树莓派](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

树莓派启动后，通过单击树莓菜单按钮打开树莓派配置工具，然后选择“首选项”，然后选择“树莓派配置”。

单击“接口”选项卡并调整串行设置，如下所示：

![显示启用串行端口和禁用串行控制台的 Raspberry Pi OS 配置屏幕的图像](images/configshot.jpg)

--- /task ---

--- 任务 --- 您还需要按照以下说明安装 buildhat python 库：

--- collapse ---
---
标题：安装 buildhat Python 库
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>在 Raspberry Pi 上打开一个终端窗口。

在提示符下键入： `sudo pip3 install buildhat`

按 <kbd>输入</kbd> 并等待“安装完成”消息。

--- /collapse ---

--- /task ---