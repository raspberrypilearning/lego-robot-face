## 简介

[[[camera-bullseye]]]

Over the course of this project you will construct a robot face from a combination of LEGO® and electronic components. You'll then use an existing machine learning model to help your face recognise different objects and react to them.

### 学习成果

--- no-print ---

Your robot face will be able to recognise and react to a range of objects. Here you can see our example of a robot face.

![Video of a robot face made out of LEGO® with LED eyes and changing expressions.](images/robot_face.gif)

You should build your robot face using whatever LEGO® and other materials you have available. We used the [LEGO® SPIKE™ Prime kit](https://education.lego.com/en-gb/product/spike-prime).

--- /no-print ---

--- print-only ---

![Picture of the completed project: a robot face made out of LEGO® with LED eyes and a smiling expression.](images/robot_face.jpg)

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

Open a terminal and use the following commands to install the needed libraries:

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

If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/robot-face/print){:target="_blank"}.

[Here is a link to the resources for this project](http://rpf.io/p/en/robot-face-go){:target="_blank"}.

--- /collapse ---

Before you begin, you'll need to have set up your Raspberry Pi computer and attached your Build HAT:

--- task ---

Mount your Raspberry Pi on to the LEGO Build Plate using M2 bolts and nuts, making sure the Raspberry Pi is on the side without the 'edge':

 ![Raspberry Pi bolted to a magenta LEGO Build Plate.](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. The Build Plate will allow you to connect the Raspberry Pi to the main structure of your dashboard more easily.

--- task ---

Line up the Build HAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"}, which makes the pins longer.)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg) ![Animation showing Buildhat fitting to Raspberry Pi](images/haton.gif)

--- /task ---

You should now power your Raspberry Pi using the 7.5V barrel jack on the Build HAT, which will allow you to use the motors.

--- task ---

If you have not already done so, set up your Raspberry Pi by following these instructions:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Once the Raspberry Pi has booted, open the Raspberry Pi Configuration tool by clicking on the Raspberry Menu button and then selecting “Preferences” and then “Raspberry Pi Configuration”.

Click on the “interfaces” tab and adjust the Serial settings as shown below:

![Image showing Raspberry Pi OS config screen with serial port enabled and serial console disabled](images/configshot.jpg)

--- /task ---

--- task --- You will also need to install the buildhat python library by following these instructions:

--- collapse ---
---
标题：安装 buildhat Python 库
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `sudo pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---
