## 들어가며

[[[camera-bullseye]]]

Over the course of this project you will construct a robot face from a combination of LEGO® and electronic components. You'll then use an existing machine learning model to help your face recognise different objects and react to them.

### 만들 작품

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
title: 준비물
---
### 하드웨어

+ 라즈베리 파이 컴퓨터
+ 라즈베리 파이 빌드 HAT
+ 라즈베리 파이 카메라 모듈
+ 30cm 라즈베리 파이 카메라 리본 케이블
+ 소형 LEGO® Technic™ 모터 2개
+ 1× 대형 LEGO® Technic™ 모터
+ 1× 미니 브레드보드
+ 12× 수-암 점퍼 와이어(20cm)
+ 2× [Adafruit 8×8 LED 매트릭스](https://www.adafruit.com/product/1049) (또는 유사 - 조립 및 수정을 위해 약간의 납땜 필요)
+ 매우 긴 스태킹 헤더 핀
+ 다양한 LEGO®( [LEGO® SPIKE™ Prime 키트](https://education.lego.com/en-gb/product/spike-prime)에서 선택 사용)
+ 20mm FM 헤더 확장기.
+ 납땜 키트

### 소프트웨어

Open a terminal and use the following commands to install the needed libraries:

+ Build HAT 제어를 위한 BuildHAT Python 라이브러리

```
sudo pip3 빌드햇 설치
```

+ TensorFlow Lite 라이브러리 및 샘플 모델 및 레이블

```
echo "deb https://packages.cloud.google.com/apt 산호-edgepu-stable 메인" | sudo 티 /etc/apt/sources.list.d/coral-edgetpu.list
컬 https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key 추가 -
sudo apt-get 업데이트
sudo apt-get install python3-tflite-runtime
```

+ Adafruit LED 매트릭스 라이브러리

```
pip3 install adafruit-circuitpython-ht16k33
```

### 다운로드

+ [이미지 분류기 테스트 파일](http://rpf.io/p/en/lego-robot-face-go){:target="_blank"}

--- /collapse ---

--- collapse ---
---
title: 배우게 될 것
---

+ LEGO®를 사용하여 더 복잡한 메커니즘을 구축하려면
+ 기계 학습 라이브러리를 사용하여 이미지를 인식하려면
+ 사전 데이터 구조를 사용하여 표정을 제어하려면

--- /collapse ---

--- collapse ---
---
title: 교육자를 위한 추가 정보
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
제목: buildhat Python 라이브러리 설치
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `sudo pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---
