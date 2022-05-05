## はじめに

[[[camera-bullseye]]]

このプロジェクトでは、 LEGO® と電子部品を組み合わせて、ロボットの顔を組み立てます。 それから既存の機械学習モデルを使用し、ロボットの顔がさまざまな物を認識して反応できるようにします。

### 作るもの

--- no-print ---

ロボットの顔は、さまざまな物を認識して反応することができます。 これがロボットの顔の例です。

![LED の目と変化する表情をもつ、 LEGO® で作られたロボットの顔のビデオ。](images/robot_face.gif)

LEGO® やその他の入手可能な素材を使って、ロボットの顔を作成していきましょう。 本項では [LEGO® SPIKE™ プライムキット](https://education.lego.com/en-gb/product/spike-prime) を使用します。

--- /no-print ---

--- print-only ---

![完成したプロジェクトの写真: LED の目と笑顔の表情をもつ、 LEGO® で作られたロボットの顔。](images/robot_face.jpg)

--- /print-only ---

--- collapse ---
---
title: 必要なもの
---
### ハードウェア

+ Raspberry Pi コンピューター
+ Raspberry Pi Build HAT
+ Raspberry Pi カメラモジュール
+ 30cmの Raspberry Pi カメラリボンケーブル
+ 2つの LEGO® Technic™ モーター
+ 1つの LEGO® Technic™ モーター
+ 1つの ミニブレッドボード
+ 12× Pin-to-socket jumper wires (20cm)
+ 2つの [Adafruit 8×8 LEDマトリックス](https://www.adafruit.com/product/1049) （または同様のもの - 組立や変更にはんだ付けが必要です）
+ 非常に長いスタッキングヘッダーピン
+ LEGO® 製品 (本項では [LEGO® SPIKE™ プライムキット](https://education.lego.com/en-gb/product/spike-prime) を使用することを前提とします)
+ 20mm pin-to-socket header extender.
+ はんだ付けキット

### ソフトウェア

ターミナルを開き、次のコマンドを使用して必要なライブラリをインストールします。

+ Build HAT を制御するための Build HAT Python ライブラリ

```
sudo pip3 install buildhat
```

+ TensorFlow Liteライブラリとサンプルモデルおよびラベル

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add-
sudo apt-get update
sudo apt-get install python3-tflite-runtime
```

+ Adafruit LED マトリックスライブラリ

```
pip3 install adafruit-circuitpython-ht16k33
```

### ダウンロード

+ [画像分類器のテストファイル](https://rpf.io/p/en/lego-robot-face-go){:target="_blank"}

--- /collapse ---

--- collapse ---
---
title: 学習すること
---

+ LEGO® を使用してより複雑なメカニズムを構築する
+ 機械学習ライブラリを使用して画像を認識する
+ 辞書のデータ構造を使用して顔の表情を制御する

--- /collapse ---

--- collapse ---
---
title: 教育者向けの追加情報
---

このプロジェクトを印刷する必要がある場合は、 [印刷用バージョン](https://projects.raspberrypi.org/en/projects/robot-face/print){:target="_ blank"}を使用してください。

[プロジェクトのリソースはこちら](https://rpf.io/p/en/lego-robot-face-go){:target="_blank"}にあります。

--- /collapse ---

開始する前に、Raspberry Piのセットアップと、Build HATの装着をしてください:

--- task ---

M2のボルトとナットを使用して、 LEGO メーカープレートの上にRaspberry Piを取り付けます。 Raspberry Piはふちがない方の面に載せます:

 ![Raspberry Pi が赤い LEGO メイカープレートに固定された様子](images/build_11.jpg)

--- /task ---

写真のとおりにRaspberry Piを固定することで、SDカードスロットが扱いやすくなります。 メイカープレートを使うことで、ダッシュボードのおもな構造に、より簡単に接続できます。

--- task ---

`This way up` の文字が見えるようにBuild HATをRaspberry Piと並べます。 全部のGPIOピンがHATにかぶるよう合わせて、しっかり押し下げてください。 (例ではピンが長くなる [スタッキングヘッダー](https://www.adafruit.com/product/2223){:target="_blank"} を使用しています。)

![GPIOピンがBuild HATから突き抜けている画像](images/build_15.jpg) ![Raspberry PiにBuildhatを搭載するアニメーション](images/haton.gif)

--- /task ---

モーターを使用するためには、Build HAT上のバレルジャックに7.5Vの電源を接続してRaspberry Piに電源を供給する必要があります。

--- task ---

まだRaspberry Piのセットアップが済んでいない場合は、次の手順に従ってセットアップしてください:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Piが起動したら、Raspberry Piメニューをクリックして“Preferences”と “Raspberry Pi Configuration”の順に選択して、Raspberry Pi Configuration toolを起動します。

“interfaces”タブをクリックして、シリアルの設定を以下のとおりに設定します:

![Raspberry Pi OS設定画面で、シリアルポートを有効にして、シリアルコンソールを無効にしている様子](images/configshot.jpg)

--- /task ---

--- task --- また、以下の手順に従って、buildhat pythonのインストールも必要になります。

--- collapse ---
---
title: buildhat Python ライブラリのインストール
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> を押して、Raspberry Pi上でターミナルウィンドウを開きます。

プロンプトで次の通りに入力します: `sudo pip3 install buildhat`

<kbd>Enter</kbd> キーを入力して "installation completed" のメッセージが表示されるまで待ちます。

--- /collapse ---

--- /task ---
