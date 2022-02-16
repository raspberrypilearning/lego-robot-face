## 소개

[[[camera-bullseye]]]

이 프로젝트를 진행하는 동안 여러분은 LEGO®와 전자 부품을 조합하여 로봇 얼굴을 구성하게 됩니다. 그런 다음 기존에 존재하는 기계 학습 모델을 사용하여 얼굴이 다양한 물체를 인식하고 이에 반응하도록 돕습니다.

### 만들 작품

--- no-print ---

로봇 얼굴은 다양한 물체를 인식하고 물체에 반응할 수 있습니다. 여기에서 로봇 얼굴의 예시를 볼 수 있습니다.

![LED 눈과 변화하는 표정을 가진 LEGO® 로 만든 로봇 얼굴의 비디오.](images/robot_face.gif)

LEGO® 및 사용 가능한 여러 재료를 사용하여 로봇 얼굴을 만들어야 합니다. 우리는 [LEGO® SPIKE™ Prime kit](https://education.lego.com/en-gb/product/spike-prime) 를 사용할 것입니다.

--- /no-print ---

--- print-only ---

![완성된 프로젝트 사진: LEGO®로 만든 로봇 얼굴 그리고 LED 눈과 웃는 표정.](images/robot_face.jpg)

--- /print-only ---

--- collapse ---
---
title: 준비물
---
### 하드웨어

+ Raspberry Pi
+ Raspberry Pi Build HAT
+ Raspberry Pi 카메라 모듈
+ 30cm Raspberry Pi 카메라 리본 케이블
+ 소형 LEGO® Technic™ 모터 2개
+ 1× 대형 LEGO® Technic™ 모터
+ 1× 미니 브레드보드
+ 12× M-F 점퍼 케이블 (20cm)
+ 2× [Adafruit 8×8 LED 매트릭스](https://www.adafruit.com/product/1049) (또는 유사한 부품 - 조립 및 수정을 위해 약간의 납땜 필요)
+ 매우 긴 스태킹 헤더 핀
+ 다양한 LEGO®([LEGO® SPIKE™ Prime 키트](https://education.lego.com/en-gb/product/spike-prime)에서 선택 사용)
+ 20mm FM 헤더 확장기.
+ 납땜 키트

### 소프트웨어

터미널을 열고 다음 명령을 사용하여 필요한 라이브러리를 설치합니다:

+ Build HAT 제어를 위한 BuildHAT Python 라이브러리

```
sudo pip3 install buildhat
```

+ TensorFlow Lite 라이브러리 및 샘플 모델 및 레이블

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-tflite-runtime
```

+ Adafruit LED 매트릭스 라이브러리

```
pip3 install adafruit-circuitpython-ht16k33
```

### 다운로드

+ [이미지 분류 모델 테스트 파일](https://rpf.io/p/ko-KR/lego-robot-face-go){:target="_blank"}

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

이 프로젝트를 인쇄하려면, [프린트용 버전](https://projects.raspberrypi.org/ko-KR/projects/robot-face/print){:target="_blank"}을 사용하십시오.

[이곳은 프로젝트에 필요한 자료를 얻을 수 있는 링크입니다.](https://rpf.io/p/ko-KR/lego-robot-face-go){:target="_blank"}

--- /collapse ---

시작하기 전에 Raspberry Pi 컴퓨터를 설정하고 Build HAT를 연결해야 합니다.

--- task ---

M2 볼트와 너트를 사용하여 LEGO Maker Plate에 Raspberry Pi를 장착하고 Raspberry Pi가 '가장자리' 쪽에 없는지 꼭 확인합니다:

 ![마젠타색 LEGO Maker Plate에 볼트로 고정된 Raspberry Pi](images/build_11.jpg)

--- /task ---

이런 식으로 Raspberry Pi를 장착하면 향후 포트와 SD 카드 슬롯에 쉽게 액세스할 수 있습니다. Maker Plate를 사용하면 Raspberry Pi를 대시보드에 더 쉽게 연결할 수 있습니다.

--- task ---

Build HAT를 Raspberry Pi와 정렬하여 `This way up` 레이블이 보이도록 합니다. 모든 GPIO 핀이 HAT로 덮여 있는지 확인하고 단단히 눌러주세요. (이 예시에서는 [스택 헤더](https://www.adafruit.com/product/2223){:target="_blank"}을 사용하므로 핀이 더 길어집니다.)

![Build HAT 상단을 관통하는 GPIO 핀의 이미지](images/build_15.jpg) ![Raspberry Pi에 적합한 Build HAT을 보여주는 애니메이션](images/haton.gif)

--- /task ---

이제 Build HAT의 7.5V 배럴 잭을 사용하여 Raspberry Pi에 전원을 공급해야 합니다. 그러면 이제부터 모터를 사용할 수 있습니다.

--- task ---

아직 설정하지 않았다면 다음 지침에 따라 Raspberry Pi를 설정하세요.

[Raspberry Pi 설정하기](https://projects.raspberrypi.org/ko-KR/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Pi가 부팅되면 Raspberry 메뉴 버튼을 클릭하고 "기본 설정(Preferences)"를 선택한 다음 "Raspberry Pi Configuration"을 선택하여 Raspberry Pi Configuration 도구를 엽니다.

"interfaces" 탭을 클릭하고 아래와 같이 시리얼 설정을 조정합니다.

![직렬 포트가 활성화되고 직렬 콘솔이 비활성화된 Raspberry Pi 구성 화면을 보여주는 이미지](images/configshot.jpg)

--- /task ---

--- task ---
또한 다음 지침에 따라 buildhat python 라이브러리를 설치해야 합니다:

--- collapse ---
---
title: buildhat Python 라이브러리 설치
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>를 눌러 Raspberry Pi에서 터미널 창을 엽니다.

커맨드 창에서 다음을 입력합니다: `sudo pip3 install buildhat`

<kbd>Enter</kbd> 를 누르고 "설치 완료" 메시지를 확인합니다.

--- /collapse ---

--- /task ---
