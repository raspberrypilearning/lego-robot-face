## Raspberry Pi を追加する

このプロジェクトでは、メイカープレートのエレメントを使って Raspberry Pi と Build HAT をマウントするのが理想的です。

![赤い LEGO® メイカープレートを示す画像。](images/build_10.png)

--- task ---

M2のボルトとナットを使用して、 LEGO メイカープレートの上にRaspberry Piを取り付けます。 Raspberry Piはふちがない方の面に載せます:

 ![Raspberry Pi が赤い LEGO® メイカープレートに固定された様子。](images/build_11.jpg)

--- /task ---

写真のとおりにRaspberry Piを固定することで、SDカードスロットが扱いやすくなります。

### カメラ とBuild HAT を取り付ける

Build HAT を追加する前に、カメラのリボンケーブルを Raspberry Pi に接続して、 Build HAT の穴に通します。 カメラボードをまだ Raspberry Pi に接続していない場合は、次の手順に従って接続します: [カメラモジュールを始めよう](https://projects.raspberrypi.org/ja-JP/projects/getting-started-with-picamera){:target="_blank"}

![Raspberry Pi カメラモジュールを Raspberry Pi に接続するアニメーション。](images/connect-camera.gif)

--- task ---

カメラリボンを Raspberry Pi に接続したまま、カメラボード側を取り外します。小さな黒いクリップを押し上げてリボンケーブルの端を緩め、リボンを引き出します:

![カメラボード背面の閉じた状態のクリップを示した画像。](images/build_12.jpg)

![開いたクリップと、リボンを取り外した状態の、カメラボードの背面を示す画像。](images/build_13.jpg)

--- /task ---

--- task ---

Build HAT の下側からリボンを差し込み、上部から引き出します。リボンがねじれていないことを確認します: ![Build HAT から突き抜けた Picamera のリボンを示す画像。](images/build_14.jpg)

--- /task ---

--- task ---

`This way up` の文字が見えるようにBuild HATをRaspberry Piと並べます。 全部のGPIOピンがHATにかぶるよう合わせて、しっかり押し下げてください。 (例ではピンが長くなる [スタッキングヘッダー](https://www.adafruit.com/product/2223){:target="_blank"}, を使用しています。)

![GPIOピンがBuild HATから突き抜けている画像](images/build_15.jpg)

--- /task ---

--- task ---
リボンケーブルの端にカメラを再度取り付けます。ねじれていないことを確認します。

![リボンケーブルが取り付けられた Picamera の画像。](images/build_16.jpg)

--- /task ---

--- task ---
黒いスタッドをいくつか使用して、メイカープレートをロボックの顔の後ろにつなぎます。 ![ロボットの顔の背面に接続された、メイカープレートと Raspberry Pi の画像。](images/build_17.jpg)

この方法で Raspberry Pi を取り付けると、ポートとピンへのアクセスが最適になり、バレルジャックを簡単に接続してロボットの顔に電力が供給できます。

--- /task ---

--- task ---

小さい LEGO® Technic™ モーターをポート A とポート B に接続して、口を制御するための準備をします。

![Build HAT のポート A とポート B に接続された 2 つの小さい LEGO® Technic™ モーターの画像。](images/build_18.jpg)

--- /task ---

--- task ---

大きい LEGO® Technic™ モーターをポート C に接続し、眉毛を制御するための準備をします。

![Build HAT のポート C に接続された大きい LEGO® Technic™ モーターの画像。](images/build_19.jpg)

--- /task ---

--- task ---

大きい LEGO® モーターを支えているフレームの上部に、ブレッドボードを裏面の粘着パッドを使用して貼り付けます。

![ロボットの顔のメカニズム上部に貼り付けられたブレッドボードを示す画像。](images/build_20.jpg)

--- /task ---

--- task ---

ホルダーの下にリボンを通し、両側のゴム栓の間にカメラをはさむようにして、ロボットの顔の上部にあるホルダーにカメラボードを取り付けます。

両側の黒いラグを使用して、カメラをゴムバンドで固定しましょう。

![前後両方にゴムバンドを使用して取り付けられたカメラボードを示す画像。](images/build_21.jpg)

--- /task ---

両方の目を Raspberry Pi の GPIO に接続するには、最初にブレッドボードに目を接続し、次にブレッドボードから GPIO ピンに接続します。

--- task ---

それぞれの目にある4つのピンを、ブレッドボード上で一緒に接続するために、オス - メスジャンパー線を8本使用します。 両方の VCC ピンがブレッドボードの同じ行にあることと、両方の GND ピンが同じ行にあることなどを確認しましょう。 そして、以下に示すように、 Raspberry Pi の 3V3 、 GND 、 SDA 、 SCL ピンに接続します。

![I2C の回路図。](images/eye_wiring.png)

--- /task ---

これでロボットの顔の作成と接続が済んだので、プログラミングの準備が整いました！





