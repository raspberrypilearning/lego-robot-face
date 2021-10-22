## 目を追加する

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">例えば、顔に使用されるLEDマトリックスはラズベリーPiに接続 <span style="color: #0faeb0">I2C</span>。 I2Cを使用するデバイスは、アドレスと呼ばれる特定の番号を使用して接続されます。 2つの行列を使用しているため、それぞれに独自のアドレスが必要になります。 </p>

--- task ---

それらを接続する前に、関連する [組み立て手順](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){：target = "_blank"}に従う必要があります。 LEDアレイの組み立てにははんだ付けが必要なため、工具を使用する前に大人の許可を得てください。 こちらのはんだ付けガイドに従ってください。 <iframe width="560" height="315" src="https://www.youtube.com/embed/8Z-2wPWGnqE" title="YouTubeビデオプレーヤー" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe>

--- /task ---

このプロジェクトで使用されるマトリックスはすべて同じアドレスを持っています。つまり、2つが連携するには、そのうちの1つに新しいアドレスが必要です。 このためには、もう少しはんだ付けが必要です。

--- task ---

あなたのはんだ付けキットを使用して、閉じ `A0` の接続 **つのみ** あなたの行列のを。

![はんだ付けされたボードとはんだ付けされていないボードの画像。](images/A0-soldering.jpg)

--- /task ---

--- task ---

ロボットの顔の四角いソケットに目を置きます。ゴムバンドを使用して固定し、ピンが上部にあることを確認します。

![LEGO®フェースに取り付けられた8x8アレイを示す画像。](images/array_eyes.jpg)

--- /task ---

ロボットの顔の基本的な構築が完了したので、Raspberry Piコンピューターを追加し、それにコンポーネントを接続する必要があります。
