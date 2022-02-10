## ラズベリーパイを追加する

For this project you'll ideally want to use the Maker Plate element to mount your Raspberry Pi and Build HAT:

![Image showing a magenta LEGO® Maker plate.](images/build_10.png)

--- task ---

Mount your Raspberry Pi onto the Maker Plate using M2 bolts and nuts, making sure the Pi is on the flat side:

 ![Raspberry Pi bolted to a magenta LEGO® Maker plate.](images/build_11.jpg)

--- /task ---

Raspberry Piをこのように取り付けると、ポートとSDカードスロットに簡単にアクセスできます。

### カメラを取り付けてHATを構築する

Build HATを追加する前に、まずカメラリボンケーブルをRaspberry Piに接続し、BuildHATの穴に通す必要があります。 カメラボードをまだRaspberryPiに接続していない場合は、次の手順に従って接続できます [カメラモジュールの使用開始](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){：target = "_blank"}。

![RaspberryPiに接続されているRaspberryPiカメラモジュールを示すアニメーション。](images/connect-camera.gif)

--- task ---

カメラリボンをRaspberryPiに接続したままにしますが、小さな黒いクリップを押し上げてリボンを引き出し、リボンの緩い端からカメラボードを取り外します。

![閉じたクリップでカメラボードの背面を示す画像。](images/build_12.jpg)

![開いたクリップとリボンを取り外した状態のカメラボードの背面を示す画像。](images/build_13.jpg)

--- /task ---

--- task ---

Build HATの下側からリボンを突き出し、上部からリボンを突き出します。リボンがねじれていないことを確認します ![BuildHATの上部を突き抜けるPicameraリボンの画像。](images/build_14.jpg)

--- /task ---

--- task ---

あなたが見ることができます確保、ラズベリーパイとビルドHATをラインアップ `までこの道を` ラベル。 すべてのGPIOピンがHATで覆われていることを確認し、しっかりと押し下げます。 （この例では、 [スタッキングヘッダー](https://www.adafruit.com/product/2223){：target = "_ blank"}を使用しているため、ピンが長くなります。）

![ビルドHATの上部を突き抜けるGPIOピンの画像。](images/build_15.jpg)

--- /task ---

---タスク--- リボンケーブルの端にカメラを再度取り付け、ねじれていないことを確認します。

![リボンケーブルに取り付けられたピカメラの画像。](images/build_16.jpg)

--- /task ---

--- task --- Connect the Maker Plate to the back of your robot face using some black studs. ![ロボットの顔の背面に接続されたメーカープレートとラズベリーパイの画像。](images/build_17.jpg)

この方法でRaspberryPiを取り付けると、ポートとピンへのアクセスが最適になり、バレルジャックを簡単に接続してロボットの顔に電力を供給することができます。

--- /task ---

--- task ---

小さなLEGO®Technic™モーターをポートAとBに接続して、口を制御する準備をします。

![BuildHATのポートAとBに接続された2つの小さなLEGO®Technic™モーターの画像。](images/build_18.jpg)

--- /task ---

--- task ---

大きなLEGO®Technic™モーターをポートCに接続し、眉毛をコントロールする準備をします。

![BuildHATのポートCに接続された大型のLEGO®Technic™モーターを示す画像。](images/build_19.jpg)

--- /task ---

--- task ---

下部の粘着パッドを使用して、大型のLEGO®モーターを支えるフレームの上部にブレッドボードを貼り付けます。

![ロボットの顔のメカニズムの上部に貼り付けられたブレッドボードを示す画像。](images/build_20.jpg)

--- /task ---

--- task ---

ホルダーの下にリボンを通し、両側のゴム栓の間にカムラをはさむことにより、ロボット面の上部にあるホルダーにカメラボードを取り付けます。

両側の黒いラグを使用して、カメラをゴムバンドで固定します。

![前後両方にゴムバンドを使用して取り付けられたカメラボードを示す画像。](images/build_21.jpg)

--- /task ---

ペアをRaspberryPi GPIOに接続するには、最初にブレッドボードを使用してアイを接続し、次にブレッドボードからGPIOピンに接続する必要があります。

--- task ---

ブレッドボード上の各目からの4つのピンを一緒に接続するために、8本のオス-メスジャンパー線を使用します。 両方のVCCピンがブレッドボードの同じ行にあること、両方のGNDピンが同じ行にあることなどを確認してください。 次に、以下に示すように、Raspberry Piの3V3、GND、SDA、およびSCLピンに接続します。

![I2C図。](images/eye_wiring.png)

--- /task ---

これでロボットの顔が作成され、接続され、プログラミングの準備が整いました。





